#A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits):
#   1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1634 (4 digits):
#   1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

import math

#function to find length of an integer
def int_length(number_cp):
    digits = int(math.log10(number_cp))+1
    return digits

#function to split an integer
def split_number(number_cp):
    result=[]
    if int_length(number_cp)==1:
        return number_cp 
    else:    
        while number_cp>0:
            result.append(number_cp%10)
            number_cp=number_cp//10

        result.reverse()    #reverse the list to obtain required result
        return result


def narcissistic(number):
    number_cp=number 
    length_number=int_length(number_cp)
    result=[]
    result=split_number(number_cp)
    summation=0
    for i in result:
        summation+=i**length_number 
    if summation==number:
        print(f"{number} is a narcissistic number ")
    else:
        print(f"{number} is not a narcissistic number ")
    

number=int(input("Enter a number: "))
narcissistic(number)