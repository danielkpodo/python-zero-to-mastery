# Know lambda expressions well
# Know list comprehensions
# Know pure functions soo well, map, filter, reduce, zip

# square the list using lambda expression

my_list = [5, 4, 3]

#  print(list(map(lambda x: x**2, my_list)))

# List Sorting
# sort using lambda using the second item
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])

print(a)
