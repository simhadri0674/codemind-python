a=int(input())
b=0
c=1
print(b,c,end=" ")
for i in range(1,a-1):
    d=b+c
    b=c
    c=d
    print(d,end=" ")