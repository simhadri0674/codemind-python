a=int(input())
if a==1:
    print("Ugly Number")
else:
    c=[]
    for i in range(2,a):
        if a%i==0:
            c.append(i)
    d=len(c)
    e=0
    for i in c:
        if i==2 or i==3 or i==5:
            e+=1
    if e==0:
        print("Not Ugly Number")
    else:
        print("Ugly Number")