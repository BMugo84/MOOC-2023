def smallest_average(person1: dict, person2: dict, person3: dict):
    result_person1 = person1["result1"] + person1["result2"] + person1["result3"] 
    average1 = result_person1/3

    result_person2 = person2["result1"] + person2["result2"] + person2["result3"] 
    average2 = result_person2/3

    result_person3 = person3["result1"] + person3["result2"] + person3["result3"] 
    average3 = result_person3/3

    smallest_avg = min(average1, average2, average3)

    if smallest_avg is average1 :
        return person1
    elif smallest_avg is average2:
        return person2
    elif smallest_avg is average3:
        return person3

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))