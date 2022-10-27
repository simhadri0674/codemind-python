x,y=map(int,input().split())
e=0
e=abs(x-y*2)
if x==0 and y%2==0:
    print("YES")

elif x==0 and y%2!=0:
    print("NO")
elif e%2==0:
    print("YES")

else:
    print("NO")