# MM-Health-Dataset

**Official Repository for**:

📄 *[From Generation to Detection: A Multimodal Multi-Task Dataset for Benchmarking Health Misinformation](https://arxiv.org/abs/2505.18685)*  
🪶 *Accepted at EMNLP 2025 Findings*

---

## Overview

**MM-Health** is a comprehensive **multimodal, multi-task dataset** designed to benchmark **health misinformation** across multiple modalities and learning paradigms.  
This repository provides both the **dataset** and **code** for reproducing experiments described in the paper.

---

## Repository Structure

```
MM-Health-Dataset
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

---

## Usage

This directory contains all source code for running the experiments presented in our paper.

1. **Setup Configuration**
   - Modify the configuration file in  
     ```
     configs/llm_config.py
     ```
   - Configure your API or model credentials.

2. **Set Model Source**
   - Specify your model source in  
     ```
     main_experiments/task_templates.py
     ```
   - Supported backends:
     - **OpenAI API**
     - **OpenRouter API**
     - **RunPod** (for self-deployed models)

3. **Run Experiments**
   ```bash
   python run_experiment.py
   ```

---

## Dataset Download link
The complete dataset is available for download through this anonymous link: https://drive.google.com/file/d/1JUun3Zk6F2E4ID9E-kiO22NhtHin6VXA/view?usp=sharing
