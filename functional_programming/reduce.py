# reduce doesn't need the list wrapper
# helps us to reduce a list into a single number or item


from functools import reduce


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, [3, 4, 10], 0))
