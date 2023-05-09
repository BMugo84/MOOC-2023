import urllib.request  # import the urllib.request module to make HTTP requests
import json  # import the json module to work with JSON data

# create a new HTTP request to the specified URL
my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

# read the data returned by the HTTP request and store it in a variable
data = my_request.read()

# print the raw data returned by the HTTP request
# print(data)

# parse the JSON data in the 'data' variable into a Python list of dictionaries
courses = json.loads(data)

# print the parsed data
# print(courses)

for item in courses:
    if item["enabled"] == True:
        sum_exercises = sum(item["exercises"])
        print(f'({item["fullName"]}, {item["name"]}, {item["year"]}, {sum_exercises})')
