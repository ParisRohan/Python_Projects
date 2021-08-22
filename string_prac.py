def string_reverse(stringA):
    string_op=""
    for i in stringA:
        string_op=i+string_op
    return string_op

stringA=input("Enter string A ")
print(string_reverse(stringA))