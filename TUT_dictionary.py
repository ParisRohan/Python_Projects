phone=input("Enter a number")
phone_dictionary={
    "0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven",
    "8":"Eight","9":"Nine"
}
output=""
for character in phone:
    output += phone_dictionary.get(character,"n.d")+" "
print(output)
