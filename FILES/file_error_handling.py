try:
    with open('./app/hey.txt', 'r') as file_object:
        current_file = file_object.read()
except FileNotFoundError as err:
    print('File does not exist')
