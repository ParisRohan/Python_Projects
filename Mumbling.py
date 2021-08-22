#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def mumbling(ip_word):
    result=" "
    counter=1
    for i in ip_word:
        result=result+i.capitalize()+i.lower()*(counter-1)+"-"
        counter+=1
    return result 

ip_word=input("Enter a word: ")
print(mumbling(ip_word))
