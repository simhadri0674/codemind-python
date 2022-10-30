a=input()
b=input()
c=a.lower()
d=b.lower()
e=list(c.split(" "))
f=list(d.split(" "))
q=0
for i in e:
    if i in f:
        q +=1
print(q)