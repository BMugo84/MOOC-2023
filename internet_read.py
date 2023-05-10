import urllib.request
import json
from math import floor

def retrieve_all() -> list:
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


def retrieve_course(course_name: str) -> dict:
    """
    Retrieves statistics for a specified course from a URL
    and returns the statistics in a dictionary format.

    Parameters:
    course_name (str): The name of the course to retrieve statistics for.

    Returns:
    A dictionary containing the statistics for the specified course.
    """

    # Open a connection to the specified course's URL
    course_url_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")

    # Read the data from the URL
    data = course_url_request.read()

    # Convert the data to a Python dictionary
    data_clean = json.loads(data)

    # Write the dictionary to a file for debugging purposes
    with open("courses.json", "w") as outfile:
        json.dump(data_clean, outfile)

    # Read the dictionary from the file
    with open("courses.json") as my_file:
        courses_json = my_file.read()

    # Convert the dictionary to a Python dictionary
    course_script = json.loads(courses_json)

    # Initialize lists to store the values for each week of the course
    students_list = []
    hours_list = []
    hour_total_list = []
    exercise_total_list = []

    # Loop through each week of the course
    for item in course_script.values():
        students = item["students"]
        hours = item["hours"]
        exercise_total = item["exercise_total"]
        hour_total = item["hour_total"]

        # Append the values for the current week to their respective lists
        students_list.append(students)
        hours_list.append(hours)
        exercise_total_list.append(exercise_total)
        hour_total_list.append(hour_total)

    # Find the number of weeks in the course
    num_weeks = len(course_script)

    # Find the maximum number of students in any week of the course
    num_students = max(students_list)

    # Find the total number of hours spent on the course
    total_hours = sum(hour_total_list)

    # Find the average number of hours spent per student
    avg_hours = floor(total_hours / num_students)

    # Find the total number of exercises completed in the course
    total_exercises = sum(exercise_total_list)

    # Find the average number of exercises completed per student
    avg_exercises = floor(total_exercises / num_students)

    # Create a dictionary containing the course statistics
    course_statistics = {
        'weeks': num_weeks,
        'students': num_students,
        'hours': total_hours,
        'hours_average': avg_hours,
        'exercises': total_exercises,
        'exercises_average': avg_exercises
    }

    # Return the course statistics dictionary
    return course_statistics

# Test the retrieve_course function with the "docker2019" course
print(retrieve_course("docker2019"))











