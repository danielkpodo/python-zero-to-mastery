# filter helps us to fish out certain datatypes based on certain conditions


def only_odd(num):
    return num % 2 != 0


print(list(filter(only_odd, [1, 2, 4, 5, 7, 9, 15, 20])))
