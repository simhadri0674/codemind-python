n=int(input())
a=1
b=0
for i in range (a, n):
    if n%i==0:
        b +=i
if b==n:
    print("True")
else:
    print("False")