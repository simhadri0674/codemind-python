a=int(input())
b=list(map(int,input().split()))
c=0
d=[]
l=set(b)
for i in l:
    if i==b.count(i):
        d.append(i)
if d==[]:
    print(-1)
else:
    print(min(d),max(d))
    