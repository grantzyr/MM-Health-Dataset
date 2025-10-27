import os
import asyncio

from tqdm.asyncio import tqdm

from .task_templates import TaskConfig
from .base_experiment import Experiment
from utils.common import read_json, save_json_file


async def run(
    splited_data_json_path: str,
    max_workers: int, 
    current_experiment: TaskConfig, 
    read_existing_result: bool = True
):
    # Configuration
    test_json_data = read_json(splited_data_json_path)
    
    # Initialize paths
    gpt_model_name_for_save = current_experiment.gpt_model_name
    if "/" in current_experiment.gpt_model_name:
        gpt_model_name_for_save = current_experiment.gpt_model_name.replace("/", "-")
    result_save_path = f"results/experiments/{current_experiment.task_name}/{current_experiment.task_name}_{current_experiment.task_data_type}{"_few_shots" if current_experiment.few_shots_articles else ""}_results_{gpt_model_name_for_save}.json"
    error_save_path = f"results/experiments/{current_experiment.task_name}/{current_experiment.task_name}_{current_experiment.task_data_type}{"_few_shots" if current_experiment.few_shots_articles else ""}_errors_{gpt_model_name_for_save}.json"

    os.makedirs(os.path.dirname(result_save_path), exist_ok=True)
    os.makedirs(os.path.dirname(error_save_path), exist_ok=True)

    # Load existing results
    try:
        classify_results = {}
        if read_existing_result:
            classify_results = read_json(result_save_path)
    except FileNotFoundError:
        print("Warning: result file doesn't exists, init with empty dict")
        classify_results = {}

    current_experiment.classify_results = classify_results
    
    experiment = Experiment(**current_experiment.model_dump())

    # Prepare list of articles to process
    print("Prepare list of articles to process...")
    articles_to_process = []
    for dataset_name, all_data in test_json_data.items():
        test_data = all_data.get('test', [])
        for i, article in enumerate(test_data):
            articles_to_process.append(((dataset_name, i), article))

    # Define concurrency limit
    semaphore = asyncio.Semaphore(max_workers)
    async def sem_process_article(task_args):
        async with semaphore:
            await experiment.process_article(task_args)

    print("start to process articles...")
    await tqdm.gather(*[sem_process_article(args) for args in articles_to_process], desc=f"{experiment.gpt_model_name[:4]} - {current_experiment.task_name} - {current_experiment.task_data_type}")
    # Sort the results
    if experiment.gpt_model_name in experiment.classify_results:
        experiment.classify_results[experiment.gpt_model_name] = experiment.sort_numeric_keys(experiment.classify_results[experiment.gpt_model_name])

    save_json_file(result_save_path, experiment.classify_results)
    if len(experiment.error_dict) > 0:
        save_json_file(error_save_path, experiment.error_dict)
    else:
        if os.path.exists(error_save_path):
            print(f"Warning: error file exists but no error, remove it: {error_save_path}")
            os.remove(error_save_path)
    print("Experiment completed.")

if __name__ == "__main__":
    asyncio.run(run())
