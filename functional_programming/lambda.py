# lambda expression are one time anonymous functions that you dont need more than once
# lambda expressions follwos this pattern
# lambda param: param * , it automatically return

# write a pure function using map to square every number in a list

from functools import reduce
my_list = [2, 4, 5, 6, 3]

print(list(map(lambda num: num**2, my_list)))

# filter a list with lambda expression

print(list(filter(lambda x: x % 2 != 0, my_list)))

# reduce with lambda functions
numbers = [10, 20, 30]

print(reduce(lambda acc, num: acc + num, numbers))

print(list(map(lambda x: x**2, numbers)))
