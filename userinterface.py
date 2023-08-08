import re
import openai
import os

openai.api_key = os.environ.get('API_KEY')
if not openai.api_key:
    raise ValueError("No API key provided. Set the API_KEY environment variable.")

MODEL = "gpt-3.5-turbo-16k-0613"

sample_text = """
Your intro text here...

1. Commercial Space Flight: Purchase a ticket with a commercial space agency when available.
2. Government Space Mission: Become an astronaut and get selected for a moon mission.
...
22. Giant Balloon Ride: Inflate a massive helium balloon and float your way to the moon (another whimsical and infeasible idea).

Your outro text here...
"""

def extract_list_items(text):
    pattern = r'^\d+\.\s*(.*)'
    items = re.findall(pattern, text, flags=re.MULTILINE)
    return items

# Prompting the user for an open-ended string
user_text = input("Please describe the topic you would like to brainstorm: ")

RES = openai.ChatCompletion.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": """
            You are a concept generator. You focus on novel conceptual related topics and subjects, not ideas for businesses. You just output ideas not explanation or conversation. You should consider all areas of a topic. Ideas can be silly or ridiculous or drawn from other domains, including fiction and myth.
            """},
            {"role": "user", "content": user_text}
        ]
    )



def baseCompletion(input):
    response = openai.Completion.create(
    engine="davinci",
    prompt=input,
    max_tokens=60,
    temperature=1.0,
    stop="\n"
    )

    return response.choices[0].text


items = extract_list_items(RES.choices[0].message["content"])


def formatListPrompt(list):
    last_line = list[-1]
    last_num = int(last_line.split(".")[0])
    new_line = "{}. New Line".format(last_num + 1)
    return s + "\n" + new_line

# Repeatedly asking the user for a list of indices
while True:
    print("Current items in the list:")
    for i, item in enumerate(items):
        print(i, ": ", item)
        
    indices_input = input("Please enter a list of indices separated by commas to remove items (or type 'exit' to quit): ")
    if indices_input.lower() == 'exit':
        break
    
    try:
        # Convert the indices to integers, sort them in descending order to remove items without changing other indices
        indices = sorted([int(index.strip()) for index in indices_input.split(',')], reverse=True)
        
        for index in indices:
            if 0 <= index < len(items):
                removed_item = items.pop(index)
                print(f"Removed item at index {index}: {removed_item}")
            else:
                print(f"Index {index} is out of range.")

        
    except ValueError:
        print("There was an error in your input. Please enter a valid list of indices separated by commas.")

print("Thank you for using the program!")

