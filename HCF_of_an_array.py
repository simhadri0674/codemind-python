def fun (a,b):
    c=a*b
    for i in range(1,b+1):
        m=a*i
        if (m%b==0):
            break
    return (c//m)
a=int(input())
l=list(map(int,input().split()))
m=2
d=fun(l[0],l[1])
while m <=(len(l)-1):
    e=fun(d,l[m])
    d=e
    m +=1
print(e)
    