#Program to convert first alphabet of each word to capital in a string

def string_capitalize(string_input):
    word=string_input.split(" ")
    result=" "
    for i in word:
        result+=i[0].capitalize()+i[1:]+" "
    return result


string_input=input("Please enter a string: ")
print(string_capitalize(string_input))