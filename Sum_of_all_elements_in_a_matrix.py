m,n=map(int,input().split())
l=[]
for i in range(m):
    k=list(map(int,input().split()))
    l.append(k)
z=0
for j in range(len(l)):
    z +=sum(l[j])
print(z)
    