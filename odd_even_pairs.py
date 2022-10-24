a=int(input())
l=list(map(int,input().split()))
#print(l)
x=[]
y=[]
for i in range(0,a):
    if l[i]%2==0:
        x.append(l[i])
    else:
        y.append(l[i])
#print(x,y)
i=1
k=0
while len(y)<=a-1:
    y.insert(i,x[k])
    i+=2
    k+=1
if len(y)%2!=0:
    y.append(0)
print(*y)
    
 