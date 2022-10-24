a=int(input())
e=0
b=0
c=0
f=0
d=0
if a<0:
    b=str(a*-1)
    c=b[::-1]
    d=int(c)*-1
    print(d)
else:
    e=str(a)
    f=e[::-1]
    print(int(f))
    