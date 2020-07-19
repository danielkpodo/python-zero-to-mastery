# you can extract the path into a variable like this
# file_path = "./app/something.txt"

with open('./app/something.txt', mode='w') as file_object:
    current_file = file_object.write("The Lord is my shepherd")
