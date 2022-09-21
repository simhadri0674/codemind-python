a=int(input())
b=1
c=0
for i in range(b,a):
    if a%i==0:
        c +=i
#print(c)       
if (c>a):
   print("True")
else:
    print("False")