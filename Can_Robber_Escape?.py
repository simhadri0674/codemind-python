a=int(input())
b=list(map(int,input().split()))
c=[]
e=0
for i in b:
    if i not in c:
        c.append(i)
if len(c)==1:
    print("YES")
else:
    for j in range(len(c)-1):
        if b.count(c[j])==b.count(c[j+1]):
            e+=1
    if e==0:
        print("NO")
    else:
        print("YES")
    
        
    