def rev(a):
    b=a[::-1]
    return b
a=input()
b=list(a.split(" "))
c=len(b)
d=[]
for i in range(c):
    if i%2==0:
        e=rev(b[i])
        d.append(e)
    else:
        f=b[i]
        d.append(f)
print(*d)