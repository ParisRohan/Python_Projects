import utilityfn

Number=[]           #get user input for list
n=int(input("Enter total number of elements within the list: "))
for i in range(0,n):
    user_ip=int(input(f"Enter number {i}: "))
    Number.append(user_ip)

print(utilityfn.find_max(Number))