a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in b:
    if b.count(i)==1:
        c.append(i)
        d+=1
if d==0:
    print(-1)
else:
    print(max(c))