def fun(a,b):
    for i in range(1,b+1):
        m=a*i
        if (m%b==0):
            break
    return m
a=int(input())
l=list(map(int,input().split()))
j=2
d=fun(l[0],l[1])
while j<=(len(l)-1):
    e=fun(d,l[j])
    d=e
    j +=1
print(e)