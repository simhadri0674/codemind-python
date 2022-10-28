def fun(a):
    r=0
    q=0
    while 1:
        x=a%10
        r=r*10+x
        a=a//10
        if len(str(r))==b:
            q=r
            break
    m=str(q)[::-1]
    return m

a,b=map(int,input().split())
e=a
c=str(a)[::-1]
d=int(c)
e=int(fun(a))
f=str(fun(d))[::-1]
g=int(f)
print(abs(e-g))

    
    
    
    