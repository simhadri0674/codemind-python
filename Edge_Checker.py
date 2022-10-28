a,b=map(int,input().split())
c=abs(a-b)
d=abs(b-a)
if (a==1 and b== 10) or   (a==10 and b==1):
    print("Yes")
elif (c==1 or d==1):
    print("Yes")
else:
    print('No')