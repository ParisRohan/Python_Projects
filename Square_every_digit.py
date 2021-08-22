#you are asked to square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

import math

#function to find length of an integer
def int_length(number):
    digits = int(math.log10(number))+1
    return digits


def split_number(number):
    result=[]
    if int_length(number)==1:
        return number
    else:
        while number>0:
            result.append(number%10)
            number=number//10
        result.reverse()
        return result 


def square_digit(number):
    result=split_number(number)
    square_multiply=" "
    for i in result:
        square_multiply+=str(i**2)
    return square_multiply


number=int(input("Enter a number: "))
print(square_digit(number))