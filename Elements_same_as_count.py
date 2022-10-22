n=int(input())
l=list(map(int,input().split()))
c=[]
e=[]
d=0
for i in l:
    if l.count(i)==i:
        c.append(i)
        d+=1
for j in c:
    if j not in e:
        e.append(j)
        
if d==0:
    print("-1")
else:
    print(*e)
        