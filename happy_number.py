a=int(input())
b=a
r=0
while b:
    x=b%10
    r+=x*x
    b=b//10
    if b==0 and r>9:
        b=r
        r=0
print(r==1)