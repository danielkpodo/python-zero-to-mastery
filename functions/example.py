# multiply all elements in an array

initial = 1

# using dependency injection instead of global keyword


def multiplier(initial, li):
    for item in li:
        initial *= item
    return initial


total = multiplier(initial, [10, 20])
print(total)
