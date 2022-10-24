a=int(input())
b=list(map(int,input().split()))
c=0
d=0
l=set(b)
for i in l:
    if i==b.count(i):
        c +=1
print(c)
        