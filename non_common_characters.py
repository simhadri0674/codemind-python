a=input()
b=a.lower()
c=input()
d=c.lower()
e=list(b.split(" "))
f=list(d.split(" "))
g=''
h=''
m=''
n=''
o=''
for i in e:
    g +=i
for j in f:
    h +=j
for i in g:
    if str(i) not in m:
        m+=i
for j in h:
    if str(j) not in n:
        n +=j
for k in m:
    if k not in n:
        o +=k
for k in n:
    if k not in m:
        o +=k
p=sorted(o)
r=''
for x in p:
    r +=x
print(r)