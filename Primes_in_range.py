def prime(i):
    c=int(i**0.5)
    if i==0 or i==1:
        return 0
    for j in range(2,c+1):
        if i%j==0:
            return 0
    return 1
a=int(input())
b=int(input())
d=0
for i in range(a,b+1):
    if prime(i):
        d +=1
print(d)
