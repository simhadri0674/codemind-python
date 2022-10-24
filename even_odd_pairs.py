a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in l:
    if i%2!=0:
        x.append(i)
    else:
        y.append(i)
i=1
k=0
while len(y)<=(a-1):
    y.insert(i,x[k])
    i +=2
    k +=1
if len(y)%2!=0:
    y.append(0)
print(*y)
