def reve(a):
    b=a
    r=0
    while b:
        x=b%10
        r=r*10+x
        b=b//10
    return r
a=int(input())
l=list(map(int,input().split()))
for i in l:
    print(reve(i),end=" ")