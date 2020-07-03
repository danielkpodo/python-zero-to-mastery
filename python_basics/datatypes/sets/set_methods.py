self_salaries = {1000, 300, 400, 490, 383, 393, 400, 20}
friend_salaries = {100, 393, 300, 400, 100, 1000}


# Useful methods
# .discard()
# .difference
# .difference_update()
# .intersection()
# .union()
# .isdisjoint()
# .issubset()
# .issuperset()


# # finds diff of self on friends
# print(self_salaries.difference(friend_salaries))

# self_salaries.discard(1000)  # removes 1000 from set
# print(self_salaries)


# # removes all instances of another set from the set
# self_salaries.difference_update(friend_salaries)
# print(self_salaries)


# check intersection, shortcut is &
print(self_salaries.intersection(friend_salaries))


# check disjoint
print(self_salaries.isdisjoint(friend_salaries))  # returns a boolean

# uinion unites both together but removes duplicates
# shortcut -> for union is |
print(self_salaries.union(friend_salaries))


# checking issubset()

ages = {18, 20}
old = {18, 20, 90, 98}
print(ages.issubset(old))


# checking issuperset()
print(ages.issuperset(old))
