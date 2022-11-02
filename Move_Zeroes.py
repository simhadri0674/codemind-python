a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i==0:
        c.append(i)
for j in b:
    if j>0:
        d.append(j)
e=[]
e=d+c
print(*e)
    