import streamlit as st

HF_API_KEY = st.secrets["HF_API_KEY"]

HF_IMAGE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

HF_IMAGE_API_URL = f"https://api-inference.huggingface.co/models/{HF_IMAGE_MODEL}"
