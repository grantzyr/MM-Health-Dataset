from .prompts import *
from utils import read_json


TEMPLATE_DICTIONARY = {
    "openai": {
        "task1_and_task2": {
            "text_image":TASK1_AND_TASK2 
        },
        "task1": {
            "text": TASK1_TEXT,
            "text_image": TASK1_TEXT_IMAGE
        },
        "task2": {
            "text": TASK2_TEXT,
            "text_image": TASK2_TEXT_IMAGE 
        },
        "task3": {
            "text": TASK3_TEXT,
            "text_image": TASK3_TEXT_IMAGE
        }
    },
    "not_openai": {
        "task1": {
            "text": TASK1_TEXT_FOR_NOT_OPENAI_V3,
            "text_image": TASK1_TEXT_IMAGE_FOR_NOT_OPENAI_V3
        },
        "task2": {
            "text": TASK2_TEXT_FOR_NOT_OPENAI_V3,
            "text_image": TASK2_TEXT_IMAGE_FOR_NOT_OPENAI_V3
        },
        "task3": {
            "text": TASK3_TEXT_FOR_NOT_OPENAI,
            "text_image": TASK3_TEXT_IMAGE_FOR_NOT_OPENAI
        }
    }
}

def get_prompt_template(provider, task_name, data_type):
    curr_provider = provider if provider == "openai" else "not_openai"
    return TEMPLATE_DICTIONARY[curr_provider][task_name][data_type]

def get_few_shots_articles(task_name: str = "task1"):
    if task_name == "task3":
        return task3_few_shots_articles
    return task1_few_shots_articles
