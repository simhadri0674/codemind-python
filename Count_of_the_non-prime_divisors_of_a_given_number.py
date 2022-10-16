def prime(i):
    if i==0 or i==1:
        return 1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 1
    return 0
    
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0 and prime(i):
        c+=1
print(c)
        