a=int(input())
b=int(input())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
c=0
for j in range(len(l)):
    c +=sum(l[j])
print(c)
    