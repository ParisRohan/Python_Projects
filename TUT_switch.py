weight=input("Enter your weight: ")
unit=input("Entered weight is in: \n (K)g or (L)bs ? ")
if unit=="K"or unit=="k":
    weight=2.025*int(weight)
    print(f"Weight : {weight}lbs")
elif unit=="L"or unit=="l":
    weight=0.5*int(weight)
    print(f"Weight : {weight}kg")
else:
    print("Please enter proper unit")
