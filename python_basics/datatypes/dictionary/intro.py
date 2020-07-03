# A dictionary is a datatype as well as a data structure
# It is an unordered key-value pair

dictionary = {
    "name": "narh",
    "age": 26,
    "school": "uhas"
}

# to access a dictionary
print(dictionary["name"])

# complex dictionary

users = [
    {"name": "narh", "age": 26, "sex": "Male"},
    {"name": "daniel", "age": 21, "sex": "Male"},
    {"name": "Agnes", "age": 36, "sex": "Female"},
]

for user in users:
    print(user.get("age"))
