#Program to check if a string is a rotated version of other string

def is_string_rotation(stringA,stringB):
    op_string=""
    op_string=stringA+stringA
    if op_string.__contains__(stringB):
       print("True")
    else:
        print("False")

stringA=input("Enter string A ")
stringB=input("Enter string B ")
is_string_rotation(stringA,stringB)