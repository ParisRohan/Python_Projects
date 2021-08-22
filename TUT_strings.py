name="Rohan Toni Paris"

print(name)         #print name string
print(name[2])      #print name string's index position 2. String starts from 0th position.
print(name[-3])     #print name string's index position 3 from end. 
print(name[3:11])   #print name string from position 3 upto position 10
print(name[:])      #print whole string

first="Rohan"
last="Paris"
age=22
msg=f"{first} {last} of age [{age}] is a software engineer"     #formatted strings
print(msg)

#use dot operator '.' for string methods
print(len(name))
print(name.upper())


