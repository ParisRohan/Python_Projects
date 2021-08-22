command=input("Enter a command : \n").lower()
if command=="help":
    print("start- to start the car \n stop- to stop the car \n quit- to exit")
while command="quit":
    command=input("Enter a command : \n").lower()
    if command=="stop":
        print("Please start the car before stopping it :)")
    elif command=="start":
        print("Car started...Ready to go !!!")
    elif command=="stop":
        print("Car stopped.")
    elif command=="quit":
        print("Exiting game :(")
        break
    else:
        print("Sorry i don't understand that :(")
