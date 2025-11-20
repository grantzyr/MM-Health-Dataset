import os

from dotenv import load_dotenv

load_dotenv("") # your dotenv file path

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
SELFHOST_API_KEY = os.getenv("SELFHOST_API_KEY")
SELFHOST_BASE_URL = os.getenv("SELFHOST_BASE_URL")
RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY")
RUNPOD_BASE_URL = os.getenv("RUNPOD_BASE_URL")