n=int(input())
d=n
b=1
c=0
for i in range(b,n):
    if n%i==0:
        c+=i
if c==n:
    print("True")
else:
    print("False")
    