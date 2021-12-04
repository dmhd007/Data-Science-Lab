f1=open("first.txt","r")
f2=open("second.txt","r")
i=0
for j in f1:
    i += 1;
    for k in f2:
        if j == k:
            print("Both the lines are same")
        else:
            print("Both  the lines are not same")
f1.close()
f2.close()