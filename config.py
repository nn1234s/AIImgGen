import os

from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "")

# You can change this model later if needed
HF_IMAGE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
HF_IMAGE_API_URL = f"https://api-inference.huggingface.co/models/{HF_IMAGE_MODEL}"