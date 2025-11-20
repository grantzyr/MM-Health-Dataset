**Official Repository for**:  
📄 *[From Generation to Detection: A Multimodal Multi-Task Dataset for Benchmarking Health Misinformation](https://arxiv.org/abs/2505.18685)*  
🪶 *Accepted at EMNLP 2025 Findings*

</div>

---

## 🔥 News

- **[Nov 2024]** MM-Health accepted at EMNLP 2025 Findings! 🎉
- **[Nov 2024]** Dataset released on [Hugging Face](https://huggingface.co/datasets/zzha6204/MM-Health)
- **[Nov 2024]** Code and evaluation scripts released

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Dataset Statistics](#dataset-statistics)
- [Tasks](#tasks)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Experiments](#experiments)
- [Dataset Download](#dataset-download)
- [Benchmark Results](#benchmark-results)
- [Citation](#citation)
- [Contact](#contact)

---

## 🎯 Overview

**MM-Health** is a comprehensive **multimodal, multi-task dataset** designed to benchmark **health misinformation detection** in the era of generative AI. The dataset addresses critical gaps in existing health misinformation datasets:

- ✅ **Large-scale**: 34,746 news articles with both text and images
- ✅ **Human + AI content**: 5,776 human-generated + 28,880 AI-generated articles
- ✅ **Multiple AI models**: 5 text generators × 5 image generators = 25 AI combinations
- ✅ **Raw content available**: Complete text and images (no dead URLs)
- ✅ **Multi-task benchmark**: Reliability check, originality check, and fine-grained AI detection

### Why MM-Health?

Existing health misinformation datasets face critical limitations:

| Issue | Previous Datasets | MM-Health |
|-------|------------------|-----------|
| AI-generated content | ❌ Mostly excluded | ✅ 28,880 AI articles |
| Multiple AI models | ❌ Single model or none | ✅ 5 text + 5 image models |
| Raw content accessibility | ❌ URLs often dead | ✅ All content accessible |
| Multimodal coverage | ⚠️ Limited | ✅ Text + images for all |

---

## ✨ Key Features

### 1. Comprehensive AI Generation
- **Text Models**: Llama-3.1-8B, Qwen2.5-7B, ChatGLM-4-9B, Gemma2-9B, Mistral-v0.3-7B
- **Image Models**: FLUX.1-dev, Stable Diffusion 1.5, SD XL, SD XL VAE, SD XL PAG

### 2. Multi-Task Benchmark
- **Task 1**: Information reliability check (reliable vs. unreliable)
- **Task 2**: Information originality check (human vs. AI vs. mixed)
- **Task 3**: Fine-grained AI detection (identify specific AI models)

### 3. Realistic Generation Pipeline
```
Human Content → GPT-4o (topic summary) → LLMs (text generation)
                     ↓
              GPT-4o (image caption) → Image models (image generation)
```

---

## 📊 Dataset Statistics

### Overall Composition

| Source | Reliable | Unreliable | Total | Images |
|--------|----------|------------|-------|--------|
| **Human** | 4,650 | 1,126 | **5,776** | 16,394 |
| **AI** | 23,250 | 5,630 | **28,880** | 111,018 |
| **Total** | **27,900** | **6,756** | **34,746** | **127,412** |

### Data Splits

| Split | Human (Reliable/Unreliable) | AI (Reliable/Unreliable) |
|-------|---------------------------|------------------------|
| Train | 3,345 / 809 | 16,725 / 4,045 |
| Val | 373 / 90 | 1,865 / 450 |
| Test | 932 / 227 | 4,660 / 1,135 |

### Four Source Datasets

1. **Med-MMHL** (2017-2023): Multi-disease coverage
2. **MM-COVID19** (Feb-Jul 2020): COVID-19 misinformation
3. **ReCOVery** (Jan-May 2020): NewsGuard labeled COVID articles
4. **MMCoVar** (Feb 2020-Mar 2021): Vaccine misinformation

---

## 🎯 Tasks

### Task 1: Information Reliability Check
Classify whether health information is **reliable** or **unreliable**.

**Input formats**:
- Text-only (human/AI separated)
- Text + Image (human/AI separated)
- Text + Image (human/AI mixed at 25%, 50%, 75%)

### Task 2: Information Originality Check
Classify whether information is **human-generated**, **AI-generated**, or **mixed**.

**Evaluation settings**:
- Zero-shot and few-shot (5-shot)
- Text-only and multimodal

### Task 3: Fine-Grained AI Detection
Identify which specific **text and image generation models** were used (25 combinations).

**Purpose**: Understand which AI models are easiest/hardest to detect.

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (for local model inference)

### Setup

```bash
# Clone the repository
git clone https://github.com/grantzyr/MM-Health-Dataset.git
cd MM-Health-Dataset

# Install dependencies
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yml
conda activate mm-health
```

### Required Packages
```
openai>=1.0.0
anthropic
pillow
numpy
pandas
torch
transformers
accelerate
```

---

## ⚡ Quick Start

### 1. Download the Dataset

**Option A: Hugging Face (Recommended)**
```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("zzha6204/MM-Health")

# Access specific subsets
med_mmhl = dataset['Med-MMHL']
mm_covid = dataset['MM-COVID19']
recovery = dataset['ReCOVery']
mmcovar = dataset['MMCoVar']
```

**Option B: Google Drive**
Download from: [Google Drive Link](https://drive.google.com/file/d/1JUun3Zk6F2E4ID9E-kiO22NhtHin6VXA/view?usp=sharing)

### 2. Configure API Keys

Edit `configs/llm_config.py`:

```python
# configs/llm_config.py
OPENAI_API_KEY = "your-openai-api-key"
OPENROUTER_API_KEY = "your-openrouter-api-key"
RUNPOD_API_KEY = "your-runpod-api-key"
```

### 3. Set Model Source

Edit `main_experiments/task_templates.py` to specify your model backend:

```python
# Choose from:
# - "openai" for OpenAI API
# - "openrouter" for OpenRouter API  
# - "runpod" for self-deployed models
MODEL_SOURCE = "openai"
```

### 4. Run Experiments

```bash
# Run all experiments
python run_experiment.py

# Run specific task
python run_experiment.py --task task1

# Run with custom config
python run_experiment.py --config configs/custom_config.py
```

---

## 📁 Repository Structure

```
MM-Health-Dataset/
├── Codes/
│   ├── configs/
│   │   ├── __init__.py
│   │   └── llm_config.py              # API keys and model configs
│   ├── llms/
│   │   ├── __init__.py
│   │   ├── custom_openai_async.py     # Async API wrapper
│   │   ├── prompt_factory.py          # Prompt management
│   │   └── prompts/
│   │       ├── task1_prompt.py        # Task 1 prompts
│   │       ├── task2_prompt.py        # Task 2 prompts
│   │       ├── task3_prompt.py        # Task 3 prompts
│   │       ├── task1_few_shots_articles.py
│   │       └── task3_few_shots_articles.py
│   ├── main_experiments/
│   │   ├── base_experiment.py         # Base experiment class
│   │   ├── experiment_models.py       # Model definitions
│   │   ├── main_experiment.py         # Main experiment runner
│   │   └── task_templates.py          # Task configurations
│   ├── utils/
│   │   ├── common.py                  # Common utilities
│   │   ├── exceptions.py              # Custom exceptions
│   │   ├── image_process.py           # Image preprocessing
│   │   └── requests.py                # API request handlers
│   └── run_experiment.py              # Main entry point
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🧪 Experiments

### Supported Models

**Proprietary Models:**
- GPT-4o (`gpt-4o-2024-08-06`)
- GPT-4o Mini (`gpt-4o-mini-2024-07-18`)

**Open-Source Models:**
- Llama-3.2-Vision (11B)
- LLaVA-1.6 (7B)
- Qwen2-VL (7.6B)

### Running Specific Tasks

```bash
# Task 1: Reliability Check
python run_experiment.py --task task1 --model gpt4o --shot 0

# Task 2: Originality Check  
python run_experiment.py --task task2 --model llama3.2 --shot 5

# Task 3: Fine-grained Detection
python run_experiment.py --task task3 --model qwen2vl --shot 5
```

### Evaluation Metrics

All tasks are evaluated using **Macro F1 Score** to account for class imbalance.

---

## 📥 Dataset Download

### Hugging Face (Recommended)
```bash
# Using huggingface-cli
huggingface-cli download zzha6204/MM-Health --repo-type dataset --local-dir ./data
```

### Google Drive
Direct download link: [Google Drive](https://drive.google.com/file/d/1JUun3Zk6F2E4ID9E-kiO22NhtHin6VXA/view?usp=sharing)

### Dataset Format

Each sample contains:
```json
{
  "id": 1044,
  "image": {
    "flux": ["path/to/flux_generated.jpg"],
    "original": ["path/to/original.jpg"],
    "sd15": ["path/to/sd15_generated.jpg"],
    // ... other image models
  },
  "text": {
    "original": "Original news article text...",
    "llama-3.1-8b": "LLM generated text...",
    "qwen2.5-7b": "LLM generated text...",
    // ... other text models
  },
  "label": "reliable" or "unreliable",
  "source": "Med-MMHL" or "MM-COVID19" or "ReCOVery" or "MMCoVar"
}
```

---

## 📈 Benchmark Results

### Task 1: Information Reliability Check (F1 Scores)

| Model | Reliable (Text+Image, Human) | Unreliable (Text+Image, Human) |
|-------|---------------------------|------------------------------|
| GPT-4o (Zero-shot) | 0.499 | 0.371 |
| GPT-4o Mini (Zero-shot) | 0.499 | 0.353 |
| Llama-3.2-V (Zero-shot) | 0.500 | 0.312 |
| LLaVA-1.6 (Five-shot) | 0.499 | 0.373 |
| Qwen2-VL (Zero-shot) | 0.500 | 0.085 |

### Task 2: Information Originality Check (F1 Scores)

| Model | Human (Zero-shot) | AI (Zero-shot) |
|-------|------------------|----------------|
| GPT-4o | 0.234 | 0.155 |
| GPT-4o Mini | 0.304 | 0.119 |
| Llama-3.2-V | 0.140 | 0.188 |
| Qwen2-VL | 0.137 | 0.271 |

### Key Findings

⚠️ **Current VLLMs struggle significantly:**
- Strong bias toward classifying content as "reliable"
- Poor performance on unreliable content detection (F1 < 0.4)
- Extremely low originality detection (F1 < 0.3)
- Fine-grained AI detection remains very challenging (F1 ≈ 0.2)

These results highlight the **urgent need for better detection methods** in the age of generative AI.

---

## 📝 Citation

If you use MM-Health in your research, please cite:

```bibtex
@inproceedings{zhang2025mmhealth,
  title={From Generation to Detection: A Multimodal Multi-Task Dataset for Benchmarking Health Misinformation},
  author={Zhang, Zhihao and Zhang, Yiran and Zhou, Xiyue and Huang, Liting and Razzak, Imran and Nakov, Preslav and Naseem, Usman},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2025},
  year={2025}
}
```

**Paper**: [arXiv:2505.18685](https://arxiv.org/abs/2505.18685)

---

## 👥 Authors

**Equal Contributors:**
- [Zhihao Zhang](https://github.com/grantzyr) - Macquarie University
- Yiran Zhang - Macquarie University

**Co-authors:**
- Xiyue Zhou - University of Sydney
- Liting Huang - University of Technology Sydney
- Imran Razzak - MBZUAI
- Preslav Nakov - MBZUAI
- [Usman Naseem](mailto:usman.naseem@mq.edu.au) - Macquarie University (Corresponding Author)

---

## 📧 Contact

For questions, issues, or collaboration inquiries:

- **Open an issue**: [GitHub Issues](https://github.com/grantzyr/MM-Health-Dataset/issues)
- **Email**: usman.naseem@mq.edu.au
- **Paper**: [arXiv:2505.18685](https://arxiv.org/abs/2505.18685)

---

## 🙏 Acknowledgments

This work builds upon several existing datasets:
- [Med-MMHL](https://github.com/styxsys0927/Med-MMHL)
- [MM-COVID19](https://github.com/mayank4490/MM-COVID19)
- [ReCOVery](https://github.com/apurvamulay/ReCOVery)
- [MMCoVaR](https://github.com/MINGCHENdev/MMCoVaR)

We thank the creators of these datasets for making their data available for research.

---

## 📄 License

This dataset is released for **research purposes only**. Please refer to individual source datasets for specific licensing terms.

---
