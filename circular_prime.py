def prime(a):
    if a==0 or a==1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 0
    return 1
a=int(input())
n=a
b=0
c=0
while a>0:
    r=a%10
    b=b*10+r
    a=a//10
for i in range(1,b+1):
    if b%i==0:
        c +=1
if prime(n) and c==2:
    print("circular prime")
elif c==2 or prime(n):
    print("prime but not a circular prime")
else:
    print("not prime")