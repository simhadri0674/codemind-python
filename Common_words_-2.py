a=input()
b=input()
c=a.lower()
d=b.lower()
e=list(c.split(" "))
f=list(d.split(" "))
q=[]
r=[]
x=0
for i in e:
    if e.count(i)==1:
        q.append(i)
for j in f:
    if f.count(j)==1:
        r.append(j)
for k in q:
    if k in r:
        x +=1
print(x)
        
        
