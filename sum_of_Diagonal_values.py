a,b=map(int,input().split())
l=[]
for i in range(a):
    c=list(map(int,input().split()))
    l.append(c)
d=0
for j in range(a):
    for k in range(b):
        if j==k or j+k==a-1 or j+k==b-1:
            d +=l[k][j]
print(d)
            
            