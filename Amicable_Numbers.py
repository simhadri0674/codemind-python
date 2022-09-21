a=int(input())
b=int(input())
c=1
d=0
for i in range(c,a):
    if a%i==0:
        d +=i
if d==b:
    print("Amicable")
else:
    print("Not Amicable")