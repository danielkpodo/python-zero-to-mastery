from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# solution 1
def capitalize_pet(pet):
    return str(pet).upper()


print(list(map(capitalize_pet, my_pets)))


# solution 2

sorted_my_numbers = sorted(my_numbers)
print(list(zip(my_strings, sorted_my_numbers)))

# solutuon 3


def over_50(score):
    return score > 50


print(list(filter(over_50, scores)))

# solution 4
scores.extend(my_numbers)
print("Scores", scores)


def accumulator(acc, num):
    return acc + num


print(reduce(accumulator, scores, 0))
