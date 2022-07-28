x=input("Enter char")
f=open("r1.txt","x")
f=open("r1.txt","w")
f.write("WELCOME")
f.close()
f=open("r1.txt","r")
temp=f.read(1)
print(temp)
if x==temp:
    print("match")
else:
    print("no")