# Another useful module is the datetime

from array import array
from time import time
import datetime

# print time format

print(datetime.time(4, 43, 9))

# useful for registration
print(datetime.date.today())


# the time module also well

# gives time in milliseconds
print(time())


# 4. Another one is an array module
# Arrays are more performat than list
# a typecode in an array is what type of data is this gonna use
# You don't wanna use a list if it is massive, instead you can consider array as an alternative to generators
arr = array("i", [1, 2, 4])
print(arr[0])
