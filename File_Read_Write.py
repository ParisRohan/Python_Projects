f=open("abc.txt","w")           #write
f.write("Rohan")
f.close()

f1=open("abc.txt","r")          #read
print(f1.read())
f1.close()

f=open("abc.txt","a")           #append
f.write(" Hello how are you :)")
f.close()