# Generators are actually iterable but not everything is a generator
# Generators are usually functions
# In generaataors instead of returning or appending we use the keyowur yield
# Yield pauses the function and do something to it when we call next

# standard way to create generator func using the range function
def generator_func(num):
    for i in range(num):
        yield i

# 1st to itenerate
# for item in generator_func(100):
#     print(item)


# using next when
g = generator_func(10)
next(g)
print(next(g))  # outputs 1


# next can called coutless times, if the number of iteraation is reached we get a stop iteraation error
# to let us know you can do this any more


# Generators are really useful calculating large set of data
