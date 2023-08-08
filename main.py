import openai
import os

openai.api_key = os.environ.get('API_KEY')
if not openai.api_key:
    raise ValueError("No API key provided. Set the API_KEY environment variable.")

MODEL = "gpt-3.5-turbo-16k-0613"

REQUEST = "Howdy do neighbor!"

res = openai.ChatCompletion.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": """
            You are a friendly assistant. Please help with this request.
            """},
            {"role": "user", "content": REQUEST}
        ]
    )


print(res.choices[0].message["content"])