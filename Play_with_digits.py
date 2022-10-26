def count(a):
    b=a
    c=0
    for i in str(a):
        c +=int(i)
        
    return c
a=int(input())
l=list(map(int,input().split()))
d=0
for i in l:
    d +=count(i)
print(d)    