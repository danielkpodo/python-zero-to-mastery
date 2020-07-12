# They are actually grouped into three
# list comprehension
# Set Comprehension
# dictionary compresension


# They are aquick way for creating list or sets or dictionsary instead of looping or appending to a bunch of list

# format [param for param in "list"]

# add all letters in a string

# using comprehension to get all letters in a string
word = "hello"

sord_strings = [char for char in word]
print(sord_strings)

# using comprehension to list all numbers in a range
# random_range = [num for num in range(1, 101)]
# print(random_range)


# squaring lists using comprehension

squared_items = [num ** 2 for num in range(1, 101)]
print(squared_items)


# filtering odd numbers in a list

only_odd = [num for num in range(100) if num % 2 != 0]
