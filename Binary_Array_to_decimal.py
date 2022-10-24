a=int(input())
l=list(map(int,input().split()))
c=l[::-1]
d=0
for i in range(0,a):
    d +=((2**i)*c[i])
    
print(d)
    