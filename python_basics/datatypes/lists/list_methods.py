# Adding items to alist
# .append() , .extend(accepts iterable), .insert(index, value) -> modifies list in place

# Removing items
# .pop() -> removes last item from a list -> returns the removed item
# .remove() -> removes a specific value from a list
# .pop(index) -> removes a particular number from a list
# .clear()

salary_of_workers = [100, 900, 893]
salary_of_workers.append(839)
print(salary_of_workers)


users = ["Derrick", "Naomi", "Irene"]
filtered_users = []
for user in users:
    if user != "Derrick":
        filtered_users.append(user)
print(filtered_users)

# Another
for user in users:
    if "Derrick" in users:
        users.remove("Derrick")
    print("Second -> ", users)

goals_scored = [10, 39, 83, 83, 84]

goals_scored.insert(3, 199)
print(goals_scored)
