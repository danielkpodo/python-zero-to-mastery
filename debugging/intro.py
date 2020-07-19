# No one writes a perffect programme
# The act of finding and removing bugs from code is called recommendation


# How to debug properly
# 1. use linting -> linting allows us to fing errors before running our code
# 2. use an ide or editor
# 3. learn to read errors
# 4. pdb -> python debugger -> favourite debugger (pdb.set_trace() -> stops here)
# pdb gives an ineractive debugger -> you can type 'help' list to see all the commands
# step allows us to step thru the code
import pdb


def add_numbers(n1, n2):
    pdb.set_trace()  # -> helps you to step thru your code
    return n1 + n2


result = add_numbers(10, 'hello')

print(result)
