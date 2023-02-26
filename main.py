import os
from dotenv import load_dotenv
import openai

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv("OPENAI_API_KEY")

input_prompt = input("Enter your image prompt: ")

# If input is empty string, exit the program
if input_prompt == "":
    print("No input given...")
    exit()

res = openai.Image.create(
    prompt=input_prompt,
    n=2,  # number of output images
    size="512x512")

image_urls = res["data"]

print(image_urls)
