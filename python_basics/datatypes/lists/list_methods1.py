# Other useful list methods are .count() and .index()

# The .count returns the number of times the object occurs in the list

salaries = [10, 10, 90, 20, 10, 10]


filter_duplicates = list(set(salaries))
print(filter_duplicates)


# .index() -> returns the index location of an item in the list
# .copy() -> also copies an entire list

# useful great methods -> .sort() and a built-in func .sorted()
# Aslo we have .reverse() -> reversing order but no  particular order

ages = [10, 290, 22, 28, 19, 8, 2, 4, 38]

ages.sort()
ages.reverse()
print(ages)


# write a function that accepts an iterable and returns the highest number in the list

def maximum_number(arr):
    list_arr = list(arr)
    list_arr.sort()
    list_arr.reverse()
    return list_arr[0]


max_number = maximum_number([1, 3, 4, 5, 5, 39, 100])
print(max_number)
