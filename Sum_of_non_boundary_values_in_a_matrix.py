a,b=map(int,input().split())
l=[]
for _ in range(a):
    c=list(map(int,input().split()))
    l.append(c)
d=0
for j in range(a):
    for k in range(b):
        if j==0 or k==0 or j==a-1 or k==b-1 :
            continue
        else:
            d +=l[j][k]
print(d)
            