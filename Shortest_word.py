#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

def find_shortest_word(ip_string):
    string_split=[]
    string_split=ip_string.split(" ")
    smallest_word=string_split[0]
    for i in string_split:
        if len(i)<len(smallest_word):
            smallest_word=i
    return smallest_word
    

ip_string=input("Enter a string: ")
smallest_word=find_shortest_word(ip_string)
print(f"Smallest word is '{smallest_word}' and its length is {len(smallest_word) } :)")