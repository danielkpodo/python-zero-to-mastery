# An iterable is a collection of items that can be looped over. Examples include
# string
# list
# dictionary
# set
# tuple

account_details = {
    "name": "narh",
    "age": 13,
    "location": "Accra"
}

# iterating over the keys
for item in account_details:
    print(item)

# iterating over the values
for item in account_details.values():
    print(item)

print("*" * 20)
# iterating over full items
for item in account_details.items():
    print(item)

# unpacking tuple in .items()
for key, value in account_details.items():
    print(key, "->", value)
