a=int(input())
l=list(map(int,input().split()))
b=int(input())
m=list(map(int,input().split()))
c=[]
for i in range(a):
    c.insert(m[i],l[i])
print(*c)