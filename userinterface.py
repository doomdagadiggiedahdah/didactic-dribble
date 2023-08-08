import re

def extract_list_items(text):
    pattern = r'^\d+\.\s*(.*)'
    items = re.findall(pattern, text, flags=re.MULTILINE)
    return items

# Prompting the user for an open-ended string
user_text = input("Please enter a string (for example, the text containing the list of ways to go to the moon): ")
items = extract_list_items(user_text)
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
