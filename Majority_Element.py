a=int(input())
l=list(map(int,input().split()))
c=set(l)
d=a//2
e=0
for i in c:
    if l.count(i)>d:
        e=i
print(e)