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

