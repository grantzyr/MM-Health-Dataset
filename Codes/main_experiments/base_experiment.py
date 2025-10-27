import json
from abc import ABC
from typing import Optional, Union, Tuple

from .experiment_models import ProgressContext, Task1ArticleClass, Task2ArticleClass
from utils.common import read_json, save_json_file
from utils.exceptions import LLMCallError, LLMGetPromptError
from llms import AsyncOpenAIClient

# Constants
TASK_NAMES = {
    "task1": {
        "name": "task1",
        "few_shots_name": "task1_few_shots",
        "attr_name": "article_type",
        "result_list": ["misinformation", "real_information"],
        "result_class": Task1ArticleClass
    },
    "task2": {
        "name": "task2",
        "few_shots_name": "task2_few_shots",
        "attr_name": "made_by",
        "result_list": ["ai", "human", "mixed"],
        "result_class": Task2ArticleClass
    },
    "task3": {
        "name": "task3",
        "few_shots_name": "task3_few_shots",
        "attr_name": "made_by",
        "result_list": ["ai", "human"],
        "result_class": Task2ArticleClass
    },
    
}


class Experiment:
    def __init__(
        self, 
        task_name: str,
        task_data_type: str,
        gpt_model_name: str,
        classify_results: dict,
        error_dict: dict,
        task_template: str, 
        provider: str, 
        mechine_id: Optional[str] = None,
        few_shots_articles: Optional[dict] = None,
        prefix_image_path: str = ""
    ) -> None:
        self.task_name: str = task_name
        self.gpt_model_name: str = gpt_model_name
        self.classify_results: dict = classify_results
        self.error_dict = error_dict
        self.task_template: str = task_template

        self.openai_client = AsyncOpenAIClient(provider=provider, mechine_id=mechine_id)
        self.is_image: bool = True if task_data_type == "text_image" else False
        self.result_list: list = TASK_NAMES[task_name]["result_list"]
        self.result_class: Union[Task1ArticleClass, Task2ArticleClass] = TASK_NAMES[task_name]["result_class"]
        self.attr_name: str = TASK_NAMES[task_name]["attr_name"]

        self.is_few_shots: bool = True if few_shots_articles else False
        self.few_shots_articles: Optional[dict] = few_shots_articles
        self.example_contents: Optional[list] = None
        self.example_groundtruths: Optional[list] = None
        self.example_image_paths: Optional[list] = None

        if self.is_few_shots:
            self.example_contents = few_shots_articles["article_contents"]
            if provider == "openai":
                self.example_groundtruths = [{self.attr_name: x} for x in few_shots_articles[f"{task_name}_groundtruth"]]
            else:
                self.example_groundtruths = [str(x) for x in few_shots_articles[f"{task_name}_groundtruth"]]
            if self.is_image:
                self.example_image_paths = few_shots_articles["image_paths"]

    async def update_error(
        self,
        progress_context: ProgressContext, 
        error_reason: str
    ):
        dataset = progress_context.dataset_name
        index = progress_context.i
        text_model = progress_context.text_model
        image_model = progress_context.image_model
        # Initialize nested dictionaries
        self.error_dict \
            .setdefault(self.gpt_model_name, {}) \
            .setdefault(dataset, {}) \
            .setdefault(index, {}) \
            .setdefault(text_model, {})
        
        if image_model:
            self.error_dict[self.gpt_model_name][dataset][index][text_model][image_model] = error_reason
        else:
            self.error_dict[self.gpt_model_name][dataset][index][text_model] = error_reason

    async def get_task_ground_truth(
        self,
        article: dict, 
        text_model: str, 
        image_model: Union[str, None]=None
    ):
        task1_label = int(article["label"])

        if not image_model:
            task2_label = 1 if text_model == "original" else 0
            return task1_label, task2_label

        if text_model == "original" and image_model == "original":
            task2_label = 1
        elif text_model != "original" and image_model != "original":
            task2_label = 0
        else:
            task2_label = 2

        return task1_label, task2_label
                
    async def parse_pred_result(self, gpt_res: dict) -> int:
        if gpt_res[self.attr_name] in self.result_list:
            return self.result_list.index(gpt_res[self.attr_name])
        raise LLMCallError(f"result error: {gpt_res}")
    
    async def check_result_exists(self, progress_context: ProgressContext) -> bool:
        try:
            if self.is_image:
                saved_result = self.classify_results[self.gpt_model_name][progress_context.dataset_name][
                    progress_context.i][progress_context.text_model][progress_context.image_model][self.attr_name]
            else:
                saved_text_model_result = self.classify_results[self.gpt_model_name][progress_context.dataset_name][
                    progress_context.i][progress_context.text_model]
                if isinstance(saved_text_model_result, dict) and "null" in saved_text_model_result:
                    self.classify_results[self.gpt_model_name][progress_context.dataset_name][
                        progress_context.i][progress_context.text_model] = saved_text_model_result["null"]
                saved_result = self.classify_results[self.gpt_model_name][progress_context.dataset_name][
                    progress_context.i][progress_context.text_model][self.attr_name]
            return saved_result in self.result_list

        except KeyError:
            return False

    async def atom_task_process(
        self, 
        progress_context: ProgressContext, 
        text_content: str,
        image_urls: Union[list, str, None] = None
    ) -> None:

        if await self.check_result_exists(progress_context):
            return

        if isinstance(image_urls, str):
            image_urls = [image_urls]

        class_for_json_model = TASK_NAMES[self.task_name]["result_class"]
        try:
            gpt_content = await self.openai_client.prepare_prompt(
                prompt_template=self.task_template,
                article_content=text_content,
                is_few_shots=self.is_few_shots,
                image_paths=image_urls,
                example_contents=self.example_contents,
                example_groundtruths=self.example_groundtruths,
                example_image_paths=self.example_image_paths,
                prefix_image_path=self.prefix_image_path
            )
            
            gpt_res, gpt_cost, completion_id = await self.openai_client.get_completion(
                prompt=gpt_content, 
                model_name=self.gpt_model_name,
                response_format_class=class_for_json_model, 
                response_attr_name=self.attr_name
            )
            
            gpt_cost_in_usd = await self.openai_client.calculate_cost(self.gpt_model_name, gpt_cost, completion_id)

            # update_gpt_res
            task1_label, task2_label = await self.get_task_ground_truth(progress_context.article, progress_context.text_model, progress_context.image_model)
            pred_result = await self.parse_pred_result(gpt_res)

            gpt_res.update({
                "cost": gpt_cost_in_usd,
                "task1_label": task1_label,
                "task2_label": task2_label,
                "pred_result": pred_result
            })
            
            if self.is_image:
                self.classify_results[self.gpt_model_name][progress_context.dataset_name][progress_context.i][progress_context.text_model][progress_context.image_model] = gpt_res
            else:
                self.classify_results[self.gpt_model_name][progress_context.dataset_name][progress_context.i][progress_context.text_model] = gpt_res

        except LLMGetPromptError as lgpe:
            print("Image Loss: ", lgpe)
            tmp_error_dict = {"Image Loss": lgpe.args[0], "Image Encode Error": lgpe.args[1]}
            error_reason = json.dumps(tmp_error_dict)
            await self.update_error(progress_context, error_reason)
        except LLMCallError as llm_call_error:
            print("GPT Error, ", progress_context.text_model, progress_context.image_model, llm_call_error)
            await self.update_error(progress_context, "GPT Error")
        except Exception as e:
            print("Unknown Error, ", progress_context.text_model, progress_context.image_model, e)
            await self.update_error(progress_context, "Unknown Error")

    # Task Processing Functions
    async def task_process(self, progress_context: ProgressContext):
        for text_model, text_content in progress_context.article['text'].items():
            if self.task_name == "task3" and text_model == "original":
                continue
            progress_context.text_model = text_model
            self.classify_results \
                .setdefault(self.gpt_model_name, {}) \
                .setdefault(progress_context.dataset_name, {}) \
                .setdefault(progress_context.i, {}) \
                .setdefault(progress_context.text_model, {})
            
            if not self.is_image:
                await self.atom_task_process(
                    progress_context=progress_context,
                    text_content=text_content,
                    image_urls=None
                )
                continue

            for image_model, image_urls in progress_context.article.get('image', {}).items():
                if self.task_name == "task3" and image_model == "original":
                    continue
                progress_context.image_model = image_model

                await self.atom_task_process(
                    progress_context=progress_context,
                    text_content=text_content,
                    image_urls=image_urls
                )

    async def process_article(self, task_args: Tuple[Tuple[str, int], dict]):
        (index, article) = task_args
        progress_context = ProgressContext(
            dataset_name=index[0],
            i=str(index[1]),
            article=article,
        )
        # Process the article
        await self.task_process(progress_context)

    def sort_numeric_keys(self, data: dict) -> dict:
        sorted_data = {}
        for dataset_name, dataset_content in data.items():
            sorted_keys = sorted(
                dataset_content.keys(),
                key=lambda x: int(x)  # Convert string to integer for sorting
            )
            sorted_content = {key: dataset_content[key] for key in sorted_keys}
            sorted_data[dataset_name] = sorted_content
        
        return sorted_data