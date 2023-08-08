import re

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
items = extract_list_items(sample_text)
print("Extracted items from the list:")
for i, item in enumerate(items):
    print(i, ": ", item)

# Repeatedly asking the user for a list of indices
while True:
    indices_input = input("Please enter a list of indices separated by commas (or type 'exit' to quit): ")
    if indices_input.lower() == 'exit':
        break
    try:
        indices = [int(index.strip()) for index in indices_input.split(',')]
        for index in indices:
            if 0 <= index < len(items):
                print(f"Item at index {index}: {items[index]}")
            else:
                print(f"Index {index} is out of range.")
    except ValueError:
        print("There was an error in your input. Please enter a valid list of indices separated by commas.")

print("Thank you for using the program!")
