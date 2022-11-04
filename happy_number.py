a=int(input())
b=a
s=0
while b:
    r=b%10
    s+=r*r
    b=b//10
    if b==0 and s>9:
        b=s
        s=0
if s!=1:
    print("False")
else:
    print("True")
    