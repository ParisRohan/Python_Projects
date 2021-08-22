#Given 3 integers A, B, C. Do the following steps-
#Swap A and B.
#Multiply A by C.
#Add C to B.
#Output new values of A and B.

a,b,c=map(int,input().split())      #code to take multiple inputs
a,b=b,a
a=a*c
b=b+c
print(a,b)