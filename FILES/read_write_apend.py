# current_file = open("./test.txt")


# print(current_file.readline())
# current_file.close()

# using the with open automatically closes the file when open

# underneath the hood open has a mode parameter = 'r' -> read
# to read and write we use -> r+
# to append to the end if a file -> a+
# to 'w' mode creates a new file if it does't exits and writes to it
# you can use the mode = '' or just use the actual mode character , e.g r, w, w+ or a

with open('sad.txt', mode='w') as file_object:
    current_file = file_object.write("God is merciful and I love him")

print(current_file)
