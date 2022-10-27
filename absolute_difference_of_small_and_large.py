a=input()
b=list(a.split(" "))
c=len(b)
d=0
e=0
for i in range(c):
    d=min(b[i])
    e=max(b[i])
    print((ord(e)-ord(d)),end=" ")
    