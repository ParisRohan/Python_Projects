def list_diff(listX,listY):
    result=[]
    counter=0
    for i in listX:
        for j in listY:
            if i!=j:
                counter+=1
        if counter==len(listY):
            result.append(i)
        counter=0
    return result 


listA=[]
listB=[]
l1=int(input("Enter size of list A: "))
l2=int(input("Enter size of list B: "))

print("Enter elements in list A:- ")
for i in range(0,l1):
    listA.append(input("> "))

print("Enter elements in list B:- ")
for i in range(0,l2):
    listB.append(input("> "))

choice=int(input("Enter 1 for 'A-B'\n Enter 2 for 'B-A' "))
if choice==1:
    print(f"A-B = {list_diff(listA,listB)}")
elif choice==2:
    print(f"B-A = {list_diff(listB,listA)}")
else:
    print("Please enter a valid choice next time :( ")
