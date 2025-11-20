import os
import json
from typing import List, Dict, Optional, Tuple, Any, Union
from dataclasses import dataclass
from pydantic import BaseModel

from openai import AsyncOpenAI

from configs.llm_config import (
    OPENAI_API_KEY, 
    OPENROUTER_API_KEY, 
    OPENROUTER_BASE_URL,
    SELFHOST_API_KEY,
    SELFHOST_BASE_URL,
    RUNPOD_API_KEY,
    RUNPOD_BASE_URL
)
from utils import (
    LLMCallError, 
    ImageEncodeError, 
    LLMGetPromptError, 
    LLMPriceCalError,
    fetch,
    encode_image
)

TASK_1_RESULT_LIST = ["real_information", "misinformation"]
TASK_2_RESULT_LIST = ["ai", "human", "mixed"]
TASK_1_FEW_SHOTS_RESULT_LIST = ["real_information", "misinformation"]
TASK_2_FEW_SHOTS_RESULT_LIST = ["ai", "human", "mixed"]

@dataclass
class GptPricing:
    input_price: float
    output_price: float
    
    async def calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        return (self.input_price * input_tokens + 
                self.output_price * output_tokens)

class GptPriceConfig:
    PRICES = {
        "gpt-4o": GptPricing(0.0000025, 0.00001),
        "gpt-4o-mini": GptPricing(0.00000015, 0.0000006)
    }
    
    @classmethod
    def get_pricing(cls, model_name: str) -> Optional[GptPricing]:
        return cls.PRICES.get(model_name, None)

class AsyncOpenAIClient:
    def __init__(self, provider: str = "openai", mechine_id: Optional[str] = None):
        self.provider = provider
        if provider == "openai":
            self.client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        elif provider == "openrouter":
            self.client = AsyncOpenAI(api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_BASE_URL)
        elif provider == "selfhost":
            self.client = AsyncOpenAI(api_key=SELFHOST_API_KEY, base_url=SELFHOST_BASE_URL)
        elif provider == "runpod":
            self.client = AsyncOpenAI(
                api_key=RUNPOD_API_KEY, 
                base_url=RUNPOD_BASE_URL.format(mechine_id=mechine_id)
            )
    
    async def calculate_cost(
        self, 
        model_name: str,
        usage: Dict[str, int],
        completion_id: Optional[str] = None
    ) -> Union[float, str]:
        if self.provider == "openai":
            pricing = GptPriceConfig.get_pricing(model_name)
            if pricing:
                return await pricing.calculate_cost(
                    usage.get('prompt_tokens', 0),
                    usage.get('completion_tokens', 0)
                )
            raise LLMPriceCalError(f"model: {model_name} not found")
        elif self.provider == "openrouter":
            # currently, openrouter cannot update the cost information 
            # as soon as it completes the model request
            # return await self._get_openrouter_cost(completion_id)
            return completion_id
        else:
            # may from runpod & selfhost, then 0
            return 0
    
    async def _get_openrouter_cost(self, completion_id: str) -> float:
        try:
            response = await fetch(
                url=f"https://openrouter.ai/api/v1/generation?id={completion_id}",
                headers={"Authorization": f'Bearer {OPENROUTER_API_KEY}'}
            )
            data = json.loads(response)
            return data['data']['total_cost']
        except:
            return completion_id
    
    async def _check_openrouter_limit(self,) -> dict:
        response = await fetch(
            url="https://openrouter.ai/api/v1/auth/key", 
            headers={"Authorization": f'Bearer {OPENROUTER_API_KEY}'}
        )
        json_res = json.loads(response.content)
        print(json_res)
        return json_res

    async def get_one_prompt_content(
        self,
        prompt_template: str,
        article_content: str,
        image_paths: Optional[List] = None,
        prefix_image_path: str = ""
    ):

        content = [{
            "type": "text", 
            "text": prompt_template.format(article_content=article_content)
        }]
        if not image_paths:
            return content
        
        file_errors = []
        encode_errors = []
        encoded_images = []
        
        # encode images (max: 5)
        for img_path in image_paths:
            if len(encoded_images) >= 5:
                break
            try:
                encoded = await encode_image(prefix_path=prefix_image_path, img_path=img_path)
                encoded_images.append(encoded)
            except FileExistsError:
                file_errors.append(img_path)
            except ImageEncodeError:
                encode_errors.append(img_path)
        
        if file_errors or encode_errors:
            raise LLMGetPromptError(file_errors, encode_errors)
        
        image_content = [
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img}",
                    "detail": "low"
                }
            }
            for img in encoded_images[:5]
        ]
        
        return content + image_content
        
    async def prepare_prompt_for_few_shots(
        self,
        prompt_template: str,
        example_contents: List[str],
        example_groundtruths: List[Dict],
        article_content: str,
        example_image_paths: Optional[List[List[str]]] = None,
        image_paths: Optional[List[str]] = None,
        prefix_image_path: str = ""
    ) -> List[Dict[str, Any]]:

        final_gpt_prompt = []
        for i, example_content in enumerate(example_contents):
            content = await self.get_one_prompt_content(
                prompt_template=prompt_template, 
                article_content=example_content, 
                image_paths=None if not example_image_paths else example_image_paths[i],
                prefix_image_path=prefix_image_path
            )
            final_gpt_prompt.append({"role": "user", "content": content})
            final_gpt_prompt.append({"role": "assistant", "content": f"{example_groundtruths[i]}"})
        
        content = await self.get_one_prompt_content(
            prompt_template=prompt_template,
            article_content=article_content,
            image_paths=image_paths,
            prefix_image_path=prefix_image_path
        )
        final_gpt_prompt.append({"role": "user", "content": content})

        return final_gpt_prompt
    
    async def prepare_prompt(
        self,
        *,
        prompt_template: str,
        article_content: str,
        is_few_shots: bool = False,
        image_paths: Optional[List[str]] = None,
        example_contents: Optional[List[str]] = None,
        example_groundtruths: Optional[List[Dict]] = None,
        example_image_paths: Optional[List[List[str]]] = None,
        prefix_image_path: str = ""
    ) -> List:
        if not is_few_shots:
            prompt = await self.get_one_prompt_content(
                prompt_template=prompt_template, 
                article_content=article_content, 
                image_paths=image_paths,
                prefix_image_path=prefix_image_path
            )
            return [{"role": "user", "content": prompt}]

        final_gpt_prompt = []
        for i, example_content in enumerate(example_contents):
            content = await self.get_one_prompt_content(
                prompt_template=prompt_template, 
                article_content=example_content, 
                image_paths=None if not example_image_paths else example_image_paths[i],
                prefix_image_path=prefix_image_path
            )
            final_gpt_prompt.append({"role": "user", "content": content})
            final_gpt_prompt.append({"role": "assistant", "content": f"{example_groundtruths[i]}"})
        
        content = await self.get_one_prompt_content(
            prompt_template=prompt_template,
            article_content=article_content,
            image_paths=image_paths,
            prefix_image_path=prefix_image_path
        )
        final_gpt_prompt.append({"role": "user", "content": content})

        return final_gpt_prompt
    
    async def get_completion(
        self,
        prompt: List,
        model_name: str,
        response_format_class: Optional[BaseModel] = None,
        response_attr_name: Optional[str] = None,
    ) -> Tuple[Optional[Dict], Optional[Dict], Optional[str]]:
        try:
            if self.provider == "openai" and response_format_class:
                completion = await self.client.beta.chat.completions.parse(
                    model=model_name,
                    messages=prompt,
                    response_format=response_format_class,
                    timeout=50
                )
                res = completion.choices[0].message.parsed

                res_json = res.model_dump()
                usage_json = completion.usage.model_dump()
                return res_json, usage_json, None

            elif self.provider == "openrouter" and response_format_class:
                completion = await self.client.chat.completions.create(
                    model=model_name,
                    messages=prompt,
                    timeout=50
                )

                completion_id = completion.id
                res = completion.choices[0].message.content
                # TODO
                res = response_format_class(made_by=res)

                res_json = res.model_dump()
                usage_json = completion.usage.model_dump()
                return res_json, usage_json, completion_id
            
            elif self.provider == "selfhost" and response_format_class:

                completion = await self.client.chat.completions.create(
                    model=model_name,
                    messages=prompt,
                    timeout=50
                )

                completion_id = completion.id
                res = completion.choices[0].message.content
                res = res.strip().lower()
                if "<" in res or ">" in res:
                    res = res.replace("<", "").replace(">", "")
                if res in TASK_1_RESULT_LIST or res in TASK_2_RESULT_LIST:
                    res = response_format_class(**{response_attr_name: res})
                else:
                    raise Exception(f"LLM result with wrong format: {res}")
                

                res_json = res.model_dump()
                usage_json = completion.usage.model_dump()
                return res_json, usage_json, completion_id
            
            elif self.provider == "runpod" and response_format_class:
                completion = await self.client.chat.completions.create(
                    model=model_name,
                    messages=prompt,
                    timeout=50
                )
                completion = json.loads(completion)
                try:
                    error_message = completion["message"]
                    print(error_message)
                except Exception as e:
                    pass
                completion_id = completion["id"]
                res: str = completion["choices"][0]["message"]["content"]
                res: str = res.strip().lower()
                if "<" in res or ">" in res:
                    res: str = res.replace("<", "").replace(">", "")
                if res in TASK_1_RESULT_LIST or res in TASK_2_RESULT_LIST:
                    res: str = response_format_class(**{response_attr_name: res})
                else:
                    raise Exception(f"LLM result with wrong format: {res}")
                

                res_json = res.model_dump()
                usage_json = completion["usage"]
                return res_json, usage_json, completion_id

            else:
                # TODO
                return None, None, None
            
        except Exception as e:
            raise LLMCallError(str(e))
