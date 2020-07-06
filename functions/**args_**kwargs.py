# *args -> allows multiple func arguments
# **kwargs -> allows multiple func keyword arguments
# **kwargs -> gives a dictionary


def add(*args):
    return sum(args)


def salary_accumulator(**kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return total


print(salary_accumulator(num=20, num2=90))


print(add(2, 3, 4, 5))

# parameter rule for funcs
# rule: params, *args, defaut parameters, **kwargs
