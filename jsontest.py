import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    description = json.loads(data)

    for item in description:
        hobbies = ", ".join(item["hobbies"])
        print(f'{item["name"]} {item["age"]} ({hobbies})')

persons = print_persons("students.json")