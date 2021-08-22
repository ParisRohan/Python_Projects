def fronttimes(string_ip,multiple,chars):
    result=""
    #for i in range(chars+1):
    result+=string_ip[:chars]
    print(result*multiple)




string_ip=input("Enter a string: ")
chars=int(input("Enter the size of substring: "))
multiple=int(input("Enter the number of times you wish to replicate the substring: "))
if chars>len(string_ip):
    print("Please enter the size of substring less than the actual entered string ")
else:
    fronttimes(string_ip,multiple,chars)
