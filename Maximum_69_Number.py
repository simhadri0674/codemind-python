a=int(input())
b=a
c=[]
while b:
    x=b%10
    c.append(x)
    b=b//10
d=c[::-1]
for i in range(len(d)):
    if d[i]==6:
        d[i]=9
        break
s=''
for i in d:
    s +=str(i)
print(s)
    
    