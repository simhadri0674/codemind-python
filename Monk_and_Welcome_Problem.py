a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
e=0
for i in range(a):
    e=b[i]+c[i]
    d.append(e)
print(*d)