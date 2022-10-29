a=int(input())
e=a//2
b=list(map(int,input().split()))
c=[]
c=b[:e+1]
f=[]
f=b[e:]
g=f[::-1]
for i in c:
    if i not in g:
        g.append(i)
print(*g)