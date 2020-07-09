# customizing and making our own list
class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))

super_list1.append("president narh")
print(super_list1[0])
