# zip helps us to join iterables together, it takes the 1st item in each list and zip them together
# zips each item in list as a tuple

# this is useful if we want to join usernames and phone numbers from a database

my_list = [2, 3, 45, 5, 6, 8]
your_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(zip(my_list, your_list)))
