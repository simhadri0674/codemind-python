def prime(d):
    if d==0 or d==1:
        return 0
    for i in range(2,int(d**0.5)+1):
        if d%i==0:
            return 0
    return 1


a=int(input())
b=int(input())
c=a+b
d=c+1
while 1:
    if prime(d):
        print(d-c)
        break
    d+=1
    