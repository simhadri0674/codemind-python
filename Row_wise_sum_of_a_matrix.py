def fun(a):
    c=0
    for i in a:
        c +=i
    return c
a,b=map(int,input().split())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
x=[]
for j in l:
    x.append(fun(j))
print(*x)

