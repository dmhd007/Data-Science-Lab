f1=open("first.txt","r")
f2=open("second.txt","w")
for i in f1:
    f2.write(i)
f1.close()
f2.close()