a=int(input())
l=list(map(int,input().split()))
c=0
for i in range(a-1):
    if l[i]>l[i+1]:
        c +=1
if c==(a-1):
    print("yes")
else:
    print("no")