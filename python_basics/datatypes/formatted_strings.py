# using formatted strings in python 3

username = "narh"
age = 26

response = f"Hello {username} you are {age}years old, when are you getting rich"
print(response)

# In python 2 they use the .format on strings

feedback = "Hello {}, you are {}years old".format(username, age)
print(feedback)
