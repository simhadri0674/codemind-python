a,b=map(int,input().split())
c=abs(a-b)
d=b-a
e=a+1
f=b-1
if a==1 and b==10:
    print("Yes")
elif a==10 and b==1:
    print("Yes")
elif c==1 or d==1:
    print("Yes")
else:
    print("No")