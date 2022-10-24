a=int(input())
b=list(map(int,input().split()))
c=0
d=[]
for j in b:
    if j not in d:
        d.append(j)
for i in d:
    print(i,b.count(i),end=" ")