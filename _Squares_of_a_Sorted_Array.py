a=int(input())
l=list(map(int,input().split()))
b=0
c=[]
for i in l:
    if i <0:
        b=i*-1
        c.append(b*b)
    else:
        c.append(i*i)
c.sort()
print(*c)
        
        
        