
# MM-Health-Supplementary-Material

## Path tree

```
Supplementary-MMHealth
└── Codes
    ├── configs
    │   ├── __init__.py
    │   └── llm_config.py
    ├── llms
    │   ├── __init__.py
    │   ├── custom_openai_async.py
    │   ├── prompt_fectory.py
    │   └── prompts
    │       ├── __init__.py
    │       ├── task1_and_task2_prompt.py
    │       ├── task1_few_shots_articles.py
    │       ├── task1_prompt.py
    │       ├── task2_prompt.py
    │       ├── task3_few_shots_articles.py
    │       └── task3_prompt.py
    ├── main_experiments
    │   ├── __init__.py
    │   ├── base_experiment.py
    │   ├── experiment_models.py
    │   ├── main_experiment.py
    │   └── task_templates.py
    ├── run_experiment.py
    └── utils
        ├── __init__.py
        ├── common.py
        ├── exceptions.py
        ├── image_process.py
        └── requests.py
```

## Usage
This directory contains all source code for running experiments.
1. setup `configs/llm_config.py`
2. setup `main_experiments/task_templates.py`, We support three model sources: openai api, openrouter api, runpod (deploy models yourself).
3. run `run_experiment.py`

## Dataset Download link
The complete dataset is available for download through this anonymous link: https://drive.google.com/file/d/1JUun3Zk6F2E4ID9E-kiO22NhtHin6VXA/view?usp=sharing
