a=int(input())
j=0
c=0
for i in range(1,a):
    if a%i==0:
        j =i+1
        if i*j==a:
            c=1
            break
if c==0:
    print("NO")
else:
    print("YES")
        
    