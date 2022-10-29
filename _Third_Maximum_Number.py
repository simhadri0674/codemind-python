a=int(input())
b=list(map(int,input().split()))
c=set(b)
i=0
e=0
f=0
if len(c)<3:
    print(max(b))
else:
    e=max(c)
    c.remove(e)
    f=max(c)
    c.remove(f)
    print(max(c))