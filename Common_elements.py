a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    if i not in c :
        c.append(i)
for j in k:
    if j not in d:
        d.append(j)
for m in c:
    if m in d:
        print(m,end=" ")