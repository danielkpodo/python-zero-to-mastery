# find the duplicates
items = ['a', 'b', 'a', 'c', 'd', 'e', 'f', "c", "f"]
duplicates = []

# Solution one
for item in items:
    if items.count(item) > 1:
        duplicates.append(item)

duplicates = list(set(duplicates))
print(duplicates)

# without using sets
