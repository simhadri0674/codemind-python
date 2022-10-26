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
a=int(input())
l=list(map(int,input().split()))
d=[]
e=0
for i in l:
    j=count(i)
    d.append(j)
c=min(d)
for i in l:
    if count(i)==c:
        e +=1
print(e)