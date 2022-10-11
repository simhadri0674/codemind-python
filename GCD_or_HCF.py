a,b=map(int,input().split())
c=0
d=a*b
for i in range(1,a+1):
    m=a*i
    if m%b==0:
        break
p=d//m
print(p)
    