# Find the highest even in a list

# solution 1
def highest_even(li):
    even_numbers = []
    for num in li:
        if num % 2 == 0:
            even_numbers.append(num)
    return max(even_numbers)


highest_even_number = highest_even(
    [2, 90, 81, 8, 5, 18, 89, 11, 113, 230, 419])

print(highest_even_number)

# solution 2


def max_even(*args):
    even_list = []
    for num in args:
        if num % 2 == 0:
            even_list.append(num)
    even_list = sorted(even_list)
    maximum_even = even_list[len(even_list) - 1]
    return maximum_even


print(max_even(1, 4, 9, 19, 145, 12, 18, 92))


# solution 3
def maximum_number_even(*args):
    even_group = []
    for num in args:
        if num % 2 == 0:
            even_group.append(num)
    even_group.sort()
    even_group.reverse()
    return even_group[0]


print(maximum_number_even(9, 19, 15, 931, 101, 100, 112, 90, 86))
