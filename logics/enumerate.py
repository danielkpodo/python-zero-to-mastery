# useful if you need the index counter of whtat you want to loop over@
# enumerate usually wraps around an iterable

users = ["Derrick", "Naomi", "Ruth", "Narh"]

for i, user in enumerate(users):
    print(i, user)


for index, number in enumerate(list(range(100))):
    print(index, number)
