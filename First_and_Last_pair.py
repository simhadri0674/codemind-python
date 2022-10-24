a=int(input())
l=list(map(int,input().split()))
for i in range(a):
    if i%2!=0:
        l.insert(i,l[-1])
        l.pop(-1)
if a%2!=0:
    l.append(0)
    print(*l)
else:
    print(*l)