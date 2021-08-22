def translate(phrase):
    result=""
    for alphabet in phrase:
        if alphabet in "AEIOUaeiou":
            result+="$"
        else:
            result+=alphabet
    return result 

phrase=input("Please enter a phrase: ")
print(translate(phrase))

