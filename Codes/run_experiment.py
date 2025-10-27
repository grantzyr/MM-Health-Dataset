import asyncio 

from main_experiments import main_experiment
from main_experiments.task_templates import *

# change the splited_data_json_path to your own data path
splited_data_json_path = "MM-Health-Data/train_test_splited_data.json"
current_experiment = llama32_experiment1_text_image
current_experiment.prefix_image_path = "../MM-Health-Data"
asyncio.run(main_experiment.run(
    splited_data_json_path=splited_data_json_path,
    max_workers=4, 
    current_experiment=current_experiment
))
