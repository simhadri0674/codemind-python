def palin(x):
    y=x
    r=0
    while y:
        z=y%10
        y//=10
        r=r*10+z
    if r==x:
        return 1
    else:
        return 0

n=int(input())
#print(n)
a=n-1
b=n+1
ac=bc=0
while 1:
    if palin(a):
        break
    a-=1
while 1:
    if palin(b):
        break
    b+=1
ac=abs(a-n)
bc=abs(b-n)
cc=min(ac,bc)
if bc==ac:
    print(a,b)
elif(cc==ac):
    print(a)
else:
    print(b)