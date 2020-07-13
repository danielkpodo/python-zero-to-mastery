# MRO -> Method Resolution Order - i rule that determines which method to run when you run a method

# you can use classname.mro() -to check for things that share similar att and methods
# The algorithm for doing Mro is called depth first search -> it is an advanced topic


# In brief mro defines the order of inheritance
# It is how python works to call methods based on hierarchy

# when things are common which one should I run

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.


def diff_array(a, b):
    a = list(a)
    b = list(b)
    diff_list = []
    for item in a:
        if item not in b:
            diff_list.append(item)
    return diff_list


a = [1, 2, 4, 4, 8]
b = [2, 4, 8]

print(diff_array(a, b))
