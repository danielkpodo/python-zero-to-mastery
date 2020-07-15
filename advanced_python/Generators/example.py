
# This is the basic of using a generator function
def simple_generator(number):
    for i in range(number):
        yield i


for item in simple_generator(10):
    print(item)
