def string_splosion(string_ip):
    result=" "
    for i in range(len(string_ip)):
        result+=string_ip[:i+1]
    print(result)


    


string_ip=input("Enter a string: ")
string_splosion(string_ip)
