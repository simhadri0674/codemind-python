n=int(input())
a=n
b=0
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==a:
    print("True")
else:
    print("False")