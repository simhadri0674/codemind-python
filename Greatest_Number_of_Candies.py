a=int(input())
l=list(map(int,input().split()))
b=int(input())
c=max(l)
d=[]
c=[(l[i]+b)>=c  for i in range(a)]
print(*c)