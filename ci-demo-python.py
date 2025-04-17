myInfo = {
"name": "Iqrash",
"age": 20,
"subjects": ["oop", "dsa", "pf", "os", "automata", "compiler", "web"]
}

friendInfo = {
"name": "Zain",
"age": 22,
"subjects": ["oop", "dsa", "compiler", "web"]
}

ageDifference=myInfo["age"]-friendInfo["age"]
if (ageDifference>0):
    print(myInfo["name"]," is older")
else:
    print(friendInfo["name"]," is older")

coursesDifference=set(myInfo["subjects"])-set(friendInfo["subjects"])
print("Courses: ",coursesDifference)