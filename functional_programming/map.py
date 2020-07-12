# useful functions that allows us to think in functional programming
# map, filter, zip, reduce

# map helps us to loop over certain number of items and receive the same number of output
def multiply_by_2(item):
    return item ** 2


print(list(map(multiply_by_2, [1, 2, 3])))


usernames = ['derrick', 'narh', 'james']


def capitalizer(name):
    return str(name).capitalize()


print(list(map(capitalizer, usernames)))
