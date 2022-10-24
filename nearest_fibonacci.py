def fab (a):
    b=0
    c=1
    m=[]
    for i in range(1,a):
        d=b+c
        b=c
        c=d
        m.append(d)
    if a in m:
        return 1
    else:
        return 0
a=int(input())
p=a-1
n=a+1
pc=nc=0
while 1:
    if fab(p):
        break
    p -=1
while 1:
    if fab (n):
        break
    n +=1
pc=abs(a-p)
nc=abs(a-n)
if fab(a):
    print(a)
elif pc ==nc:
    print(p,n)
elif pc < nc:
    print(p)
else:
    print(n)