# sum up the total of this list using looping

from functools import reduce
items = [1, 3, 4, 5, 6, 7, 7, 5, 7, 6, 6, 3]

total = 0
for num in items:
    total += num
print(total)

print(sum(items))

# Higher order functions


def summer(accumulator, initial):
    return accumulator + initial


result = reduce(summer, items)
print(result)
