a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
d=0
e=0
for j in range(a):
    c=0
    for m in range(b):
        if (l[j][m])%2==0:
            d +=l[j][m]
        else:
            e +=l[j][m]
print(d,e)
            
