# Error handling allows our script to continue running even if there is an error.
# We use try except in handling errors in python
# We can use multiple except blocks to handle different errors
# using only except: means any type of error
# A good practice us catch based on specific exception, this way you know what the error is and you cn be d
# descriptive

# while True:
#     try:
#         age = int(input('What is your age '))
#         print(f"You are {500/ age}yrs old")

#     except ValueError:
#         print("Please enter a number")

#     except ZeroDivisionError:
#         print("Denometer divided by zero is not alowed")
#     else:
#         break


# Outputting errors

def add_numbers(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Operation is not possible: {err}")


print(add_numbers(10, "3"))

# Multiple uscases for errors


def divider(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError):  # you can also add (as err, and print err)
        print("Ooooops!!, Something happened")


print(divider(10, "1"))
