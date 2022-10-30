a=input()
b=a.lower()
c=input()
d=c.lower()
e=list(b.split(" "))
f=list(d.split(" "))
g=''
h=''
q=0
m=''
n=''
for i in e:
    g +=i
for j in f:
    h +=j
for i in g :
    if str(i) not in m:
        m +=i
for j in h :
    if str(j) not in n:
        n +=j
for k in m:
    if k not in n:
        q +=1
for k in n:
    if k not in m:
        q +=1
print(q)