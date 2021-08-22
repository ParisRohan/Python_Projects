name=input("Enter a name ")
L=len(name)

if L<3:
    print("Entered name must be atleast 3 characters long")
elif L>50:
    print("Entered name can be a max of 50 characters")
else:
    print("Name looks good !")
