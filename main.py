import reparse
import openai
import os

openai.api_key = os.environ.get('API_KEY')
if not openai.api_key:
    raise ValueError("No API key provided. Set the API_KEY environment variable.")

MODEL = "gpt-3.5-turbo-16k-0613"

REQUEST = input("What would you like to think about today?\n")

res = openai.ChatCompletion.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": """
            You are a concept generator. You focus on novel conceptual related topics and subjects, not ideas for businesses. You just output ideas not explanation or conversation. You should consider all areas of a topic. Ideas can be silly or ridiculous or drawn from other domains, including fiction and myth.
            """},
            {"role": "user", "content": REQUEST}
        ]
    )


print(reparse.extract_list_items(res.choices[0].message["content"]))

# print(res.choices[0].message["content"])