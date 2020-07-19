# We have specialized datatypes

# 1. collection module

from collections import Counter, defaultdict, OrderedDict

# The Counter creates a dictionary that keeps track of how many times an item occurs in an iterable
li = [1, 1, 1, 3, 4, 5, 5, 6, 3, 5, 3, 2]

print(Counter(li))

# You can also check it on sentences

sentence = "daniel daniel daniel is sthe swordd off destiny gibbrish"
print(Counter(sentence))


# Using defaultdict -> allows us to use a callable obj to give a default value to a dictionary

dictionary = {
    "username": "daniel",
    "age": 23
}

user_dict = defaultdict(lambda: "does not exist", dictionary)
print(user_dict['apple'])


# OrderedDict retains the order that you insert into a dictionary
# Now a days python has made ordered dict default in python
d1 = OrderedDict({
    'a': 1,
    'b': 3
})

d2 = OrderedDict({
    'b': 3,
    'a': 1
})

print(d1 == d2)  # checks the order of insertion does will output as False
