import random  # import the random module for generating random values

# loop 10 times
for i in range(10):
    value = random.randint(1,6)  # generate a random integer between 1 and 6 and assign it to the value variable

names = ["John", "james", "Sheila", "Karen", "Dan", "Lisa", "Bob"]  # create a list of names

random.shuffle(names)  # shuffle the names list randomly

# loop 10 times
for i in range(10):
    names = ["John", "james", "Sheila", "Karen", "Dan", "Lisa", "Bob"]  # reset the names list to its original values
    random.shuffle(names)  # shuffle the names list randomly again

names = ["John", "james", "Sheila", "Karen", "Dan", "Lisa", "Bob"]  # create a list of names

# loop 10 times
for i in range(10):
    group = random.sample(names, 3)  # randomly select 3 names from the names list and assign them to the group variable
