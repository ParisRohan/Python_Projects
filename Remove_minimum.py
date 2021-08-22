#Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.
#Don't change the order of the elements that are left.

def delete_minimum(listA):
    minimum=min(listA)
    listA.remove(minimum)
    return listA

    
listA=[]
l1=int(input("Enter the length of the list: "))
print("Enter elements below-> ")
for i in range(0,l1):
    listA.append(input("> "))
print(delete_minimum(listA))