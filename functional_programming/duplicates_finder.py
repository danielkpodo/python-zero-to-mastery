items = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []

for item in items:
    if items.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(duplicates)

# solution 2

duplicates_list = list({item for item in items if items.count(item) > 1})
print(duplicates_list)
