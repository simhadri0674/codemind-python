n=int(input())
a=0
b=0
for i in str(n):
    if int(i)%2==0:
        a +=1
    if int(i)%2!=0:
        b +=1
if a >=1 and b>=1 :
    print("Mixed")
elif a>=1 and b==0:
    print("Even")
else:
    print("Odd")