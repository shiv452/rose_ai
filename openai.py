import openai
from config import apikey  # Make sure your 'config.py' file contains the correct API key
import os

openai.api_key = apikey

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  # 'model' should be 'engine'
    prompt="what is the color of mango?",  # Corrected the prompt for clarity
    temperature=0.7,
    max_tokens=256,  # 'max_token' should be 'max_tokens'
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0  # Corrected 'presense_penalty' to 'presence_penalty'
)

print(response)
