# SETS - we can do the same thing we did for lists we just change it to { }

salaries = {num for num in range(200, 221)}
print(salaries)

salaries_increase = {num**2 for num in range(200, 221)}
print(salaries_increase)


# dictionary comprehension
#  {key:value for item in dict}
# {key:value**2 for item in dict}


users = {
    "narh": 100,
    "derrick": 39,
    "renee": 23
}

# doubling the values for users
squares_users = {key: value**2 for key, value in users.items()}
print(squares_users)


# maintaining the key and doubling value in a list using dict

example = {num: num*2 for num in [1, 2, 4]}
print(example)
