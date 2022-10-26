def count(a):
    b=e=0
    c=f=0
    d=0
    if a<=0:
        b=a*-1
        c=str(b)
        d=len(c)
        return d
    else:
        e=str(a)
        f=len(e)
        return f
a,b=map(int,input().split())
l=list(map(int,input().split()))
d=0
for i in l:
    if count(i)==b:
        d +=1
print(d)
    