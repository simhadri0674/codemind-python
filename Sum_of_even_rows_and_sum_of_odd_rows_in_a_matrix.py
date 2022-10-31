a,b=map(int,input().split())
c=[]
for i in range(a):
    d=list(map(int,input().split()))
    c.append(d)
od=0
ev=0
for i in range(len(c)):
    if i&1:
        od +=sum(c[i])
    else:
        ev +=sum(c[i])
print(ev,od)    