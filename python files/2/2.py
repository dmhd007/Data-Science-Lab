f1=open("first.txt","r")
count=0
for i in f1:
    if i !="\n":
        count += 1
f1.close()
print(count)