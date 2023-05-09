import json

def print_persons(filename: str):
    """
    Reads a JSON file containing information about students and prints their name, age and hobbies.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        None
    """
    with open(filename) as my_file:
        data = my_file.read()

    description = json.loads(data)

    for item in description:
        hobbies = ", ".join(item["hobbies"])
        print(f'{item["name"]} {item["age"]} years ({hobbies})')

print_persons("students.json")
