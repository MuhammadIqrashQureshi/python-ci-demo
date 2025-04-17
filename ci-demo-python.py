my_info = {
    "name": "Iqrash",
    "age": 20,
    "subjects": ["oop", "dsa", "pf", "os", "automata", "compiler", "web"]
}

friend_info = {
    "name": "Zain",
    "age": 22,
    "subjects": ["oop", "dsa", "compiler", "web"]
}

age_difference = my_info["age"] - friend_info["age"]
if age_difference > 0:
    print(my_info["name"], "is older")
else:
    print(friend_info["name"], "is older")

courses_difference = set(my_info["subjects"]) - set(friend_info["subjects"])
print("Courses: ", courses_difference)
