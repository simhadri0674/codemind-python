a,b=map(int,input().split())
c=a*b
for i in range(1,b+1):
    m=a*i
    if m%b==0:
        break
print(m)
    