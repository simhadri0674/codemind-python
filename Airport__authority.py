l=[]
for i in range(int(input())):
    a=int(input())
    l.append(a)
b=int(input())
c=0
for i in l:
    if i <=b:
        c +=1
    else:
        c +=2
print(c)
    