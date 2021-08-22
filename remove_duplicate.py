#Program to remove duplicate entries from a given string

def remove_duplicate(string_ip):
    string_op=""
    words=string_ip.split(" ")
    for i in words:
        if i not in string_op:
            string_op+=i+" "

    print(string_op)
string_ip=input("Enter a string ")
remove_duplicate(string_ip)