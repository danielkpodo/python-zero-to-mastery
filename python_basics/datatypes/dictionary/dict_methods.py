# To avoid errors in your when accessing keys use a .get() to access

dictionary = {
    "user": "Frank",
    "age": 23,
    "malaria": "danny"
}

# Not common way of creating dictionaries
user = dict(name="Akilla")
print(user)

# Useful dictionary methods -> .copy(), .pop(), .popitem(), .values(), .items, .keys()

print(dictionary.keys())  # returns a list of keys
print(dictionary.values())  # returns a list of values
print(dictionary.items())

dictionary.pop("malaria")  # removes specified key
print(dictionary)

cloned_dictionary = dictionary.cop()
print(cloned_dictionary)
