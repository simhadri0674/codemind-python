a,b=map(int,input().split())
l=[]
e=[]
f=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
for j in range(b):
    c=0
    for m in range(len(l)):
        c +=(l[m][j])
    e.append(c)
print(max(e))
        