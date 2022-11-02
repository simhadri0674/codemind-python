a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
c=0
for i in range(a):
    for j in range(b):
        if i==j or i+j==a-1:
            c+=l[i][j]
            #print(l[i][j])
print(c)
        