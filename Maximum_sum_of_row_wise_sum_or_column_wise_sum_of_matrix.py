a,b=map(int,input().split())
l=[]
e=[]
f=[]
x=0
y=0
c=0
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
for m in range(len(l)):
    c=sum(l[m])
    e.append(c)
for n in range(b):
    d=0
    for o in range(len(l)):
        d +=(l[o][n])
    f.append(d)
x=max(e)
y=max(f)
if x>y:
    print(x)
else:
    print(y)