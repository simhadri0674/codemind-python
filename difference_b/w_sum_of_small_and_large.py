a=input()
b=list(a.split(" "))
c=len(b)
d=0
e=0
h=j=0
f=[]
g=[]
for i in range(c):
    d=min(b[i])
    g.append(ord(d))
for i in range(c):
    e=max(b[i])
    f.append(ord(e))
print((sum(f)-sum(g)))