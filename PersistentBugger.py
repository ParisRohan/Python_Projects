#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
#For example:
#persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
#persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
#persistence(4) => 0   # Because 4 is already a one-digit number.

import math

#function to find length of an integer
def int_length(number):
    digits = int(math.log10(number))+1
    return digits

#function to split an integer
def split_number(number):
    result=[]
    if number==0:
        return 0
    else:    
        while number>0:
            result.append(number%10)
            number=number//10

        result.reverse()    #reverse the list to obtain required result
        return result


def persistence(number):
    if int_length(number)==1:
        return 0
    else:
        count=0
        while int_length(number)>1:
            result=split_number(number)
            number=1 
            for i in result:
                number=number*i
            count+=1
        return count

    
number=int(input("Enter a number: "))
number_copy=number 
print(f"Multiplicative persistence of {number} = {persistence(number_copy)}")


