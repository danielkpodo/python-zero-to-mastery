# break breaks you totally out of the loop
# continue takes you back to the top of the enclosing loop
# pass acts as a placeholder


for num in list(range(100)):
    if num % 2 == 0:
        continue
    print(num)
