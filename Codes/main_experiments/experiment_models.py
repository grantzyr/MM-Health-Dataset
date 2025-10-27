from typing import Optional, Union, Dict
from pydantic import BaseModel

class Task1ArticleClass(BaseModel):
    article_type: str

class Task2ArticleClass(BaseModel):
    made_by: str

class TaskConfig(BaseModel):
    task_name: str
    task_data_type: str
    gpt_model_name: str
    classify_results: dict
    error_dict: dict
    task_template: str
    provider: str
    mechine_id: Optional[str] = None
    few_shots_articles: Optional[dict] = None
    prefix_image_path: str = ""

class ProgressContext(BaseModel):
    dataset_name: Optional[str] = None
    i: Optional[str] = None
    article: Union[str, Dict, None] = None
    text_model: Optional[str] = None
    image_model: Optional[str] = None