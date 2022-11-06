import os
from dotenv import load_dotenv
import openai

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv("OPENAI_API_KEY")

res = openai.Image.create(
    prompt="A depiction of life in year 3040",
    n=1,  # number of output images
    size="512x512")

image_urls = res["data"]

print(image_urls)
