a=int(input())
l=list(map(int,input().split()))
c=sum(l)
if c%4==0:
    print("X")
else:
    print("Y")