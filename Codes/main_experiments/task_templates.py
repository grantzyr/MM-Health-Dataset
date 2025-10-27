from .experiment_models import TaskConfig
from llms import get_prompt_template, get_few_shots_articles

LLAMA_MECHINE_ID = ""
LLAMA_MODEL_NAME = ""
LLAMA_PROVIDER = "runpod"
llama32_experiment1_text = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task1", "text"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = None
)

llama32_experiment1_text_image = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task1", "text_image"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = None
)

llama32_experiment2_text = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task2", "text"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = None
)

llama32_experiment2_text_image = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task2", "text_image"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = None
)

llama32_experiment3_text_image = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task3", "text_image"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = None
)

llama32_experiment1_text_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task1", "text"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text"]
)

llama32_experiment1_text_image_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task1", "text_image"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text_image"]
)

llama32_experiment2_text_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task2", "text"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text"]
)

llama32_experiment2_text_image_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task2", "text_image"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text_image"]
)

llama32_experiment3_text_image_5_shots = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = LLAMA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAMA_PROVIDER, "task3", "text_image"),
    provider = LLAMA_PROVIDER,
    mechine_id = LLAMA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task3")["text_image"]
)

QWEN_MECHINE_ID = ""
QWEN_MODEL_NAME = ""
QWEN_PROVIDER = "runpod"
qwen_experiment1_text = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task1", "text"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = None
)

qwen_experiment1_text_image = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task1", "text_image"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = None
)

qwen_experiment2_text = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task2", "text"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = None
)

qwen_experiment2_text_image = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task2", "text_image"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = None
)

qwen_experiment3_text_image = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task3", "text_image"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = None
)

qwen_experiment1_text_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task1", "text"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text"]
)

qwen_experiment1_text_image_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task1", "text_image"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text_image"]
)

qwen_experiment2_text_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task2", "text"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text"]
)

qwen_experiment2_text_image_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task2", "text_image"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text_image"]
)

qwen_experiment3_text_image_5_shots = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = QWEN_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(QWEN_PROVIDER, "task3", "text_image"),
    provider = QWEN_PROVIDER,
    mechine_id = QWEN_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task3")["text_image"]
)


LLAVA_MECHINE_ID = ""
LLAVA_MODEL_NAME = ""
LLAVA_PROVIDER = "runpod"
llava_experiment1_text = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task1", "text"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = None
)

llava_experiment1_text_image = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task1", "text_image"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = None
)

llava_experiment2_text = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task2", "text"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = None
)

llava_experiment2_text_image = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task2", "text_image"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = None
)

llava_experiment3_text_image = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task3", "text_image"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = None
)

llava_experiment1_text_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task1", "text"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text"]
)

llava_experiment1_text_image_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task1", "text_image"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text_image"]
)

llava_experiment2_text_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task2", "text"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text"]
)

llava_experiment2_text_image_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task2", "text_image"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text_image"]
)

llava_experiment3_text_image_5_shots = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = LLAVA_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LLAVA_PROVIDER, "task3", "text_image"),
    provider = LLAVA_PROVIDER,
    mechine_id = LLAVA_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task3")["text_image"]
)


LAST_MECHINE_ID = ""
LAST_MODEL_NAME = ""
LAST_PROVIDER = "selfhost"
last_experiment1_text = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task1", "text"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = None
)

last_experiment1_text_image = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task1", "text_image"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = None
)

last_experiment2_text = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task2", "text"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = None
)

last_experiment2_text_image = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task2", "text_image"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = None
)

last_experiment3_text_image = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task3", "text_image"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = None
)

last_experiment1_text_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task1", "text"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text"]
)

last_experiment1_text_image_5_shots = TaskConfig(
    task_name = "task1",
    task_data_type = "text_image",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task1", "text_image"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task1")["text_image"]
)

last_experiment2_text_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task2", "text"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text"]
)

last_experiment2_text_image_5_shots = TaskConfig(
    task_name = "task2",
    task_data_type = "text_image",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task2", "text_image"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task2")["text_image"]
)

last_experiment3_text_image_5_shots = TaskConfig(
    task_name = "task3",
    task_data_type = "text_image",
    gpt_model_name = LAST_MODEL_NAME,
    classify_results = {},
    error_dict = {},
    task_template = get_prompt_template(LAST_PROVIDER, "task3", "text_image"),
    provider = LAST_PROVIDER,
    mechine_id = LAST_MECHINE_ID,
    few_shots_articles = get_few_shots_articles("task3")["text_image"]
)