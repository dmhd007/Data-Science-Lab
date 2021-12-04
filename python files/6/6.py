f1=open("first.txt","r")
line=f1.readlines()
f1.close()

f2=open("first.txt","w")
for lines in line:
    if lines.strip("\n") != "Vyshak":
        f2.write(lines)

f2.close()