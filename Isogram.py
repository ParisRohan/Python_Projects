#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#Example->
#is_isogram("Dermatoglyphics" ) == true
#is_isogram("aba" ) == false
#is_isogram("moOse" ) == false # -- ignore letter case

def is_isogram(string_input):
    c=0
    for i in string_input:
        if string_input.count(i)==1:
            c+=1
    if c==len(string_input):
        print(f"{string_input} is a isogram :) ")
    else:
        print(f"{string_input} is not a isogram :( ")


string_input=input("Please enter a string: ")
is_isogram(string_input)
