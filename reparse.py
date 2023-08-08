import re

def extract_list_items(text):
    # Regular expression pattern to match lines that start with a digit followed by a period
    pattern = r'^\d+\.\s*(.*)'
    
    # Find all matches using the pattern
    items = re.findall(pattern, text, flags=re.MULTILINE)
    
    return items

# text = """
# Your intro text here...

# 1. Commercial Space Flight: Purchase a ticket with a commercial space agency when available.
# 2. Government Space Mission: Become an astronaut and get selected for a moon mission.
# ...
# 22. Giant Balloon Ride: Inflate a massive helium balloon and float your way to the moon (another whimsical and infeasible idea).

# Your outro text here...
# """

# items = extract_list_items(text)

# for item in items:
#     print(item)

