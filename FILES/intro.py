
# IO stands for input and output
# when of the ways we use io is through reading files
# python has a built in module that allows us to read and write to files
# the open funtion has this idea of a cursor that is you can only read the file once
# A work around this is to use .seek(0) -> moves cursor to whatever index,


# .readline() -. only gives the first line
# .readlines() -> gives a list that conatins all the lines
# without  using with we have to manually close the -> .close() => we have to manually close the file

with open("./test.txt") as file_object:
    working_file = file_object.read()

print(working_file)
print(working_file)
print(working_file)
