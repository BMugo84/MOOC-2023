import urllib.request
import json

def retrieve_all():
    """
    Retrieves the data of all courses that are currently active.

    Returns:
        A list of tuples, where each tuple contains the name of the course, name, year,
        and the sum of the values listed in exercises.
    """
    # create a new HTTP request to the specified URL
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    # read the data returned by the HTTP request and store it in a variable
    data = my_request.read()

    # parse the JSON data in the 'data' variable into a Python list of dictionaries
    courses = json.loads(data)

    active = []
    # iterate over the list of courses
    for item in courses:
        # check if the course is enabled
        if item["enabled"]:
            # calculate the sum of the exercises
            sum_exercises = sum(item["exercises"])
            # create a tuple with the required fields and append it to the 'active' list
            tup = (item["fullName"], item["name"], item["year"], sum_exercises)
            active.append(tup)
    return active

# print the list of active courses
print(retrieve_all())
