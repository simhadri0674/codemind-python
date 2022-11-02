a,b=map(int,input().split())
l=[]
c=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
for j in range(b):
    e=0
    f=[]
    for m in range(len(l)):
        e=(l[m][j])
        f.append(e)
    print(max(f))
    