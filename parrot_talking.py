def parrot_trouble(is_talking,hour):
    if is_talking.lower()=="true" and (hour<7 or hour>20):
        print("TROUBLE !!!")
    else:
        print("No Trouble :)")


is_talking=input("Is the parrot talking? \n True/False: ")
hour=int(input("What is current hour? "))
parrot_trouble(is_talking,hour)


