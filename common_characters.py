a=input()
b=a.lower()
c=input()
d=c.lower()
e=list(b.split(" "))
f=list(d.split(" "))
g=''
h=''
q=''
m=''
n=''
for i in e:
    g +=i
for j in f:
    h +=j
for i in g:
    if str(i) not in m:
        m +=i
for j in h:
    if str(j) not in n:
        n +=j
for k in m:
    if k in n:
        q +=k
r=sorted(q)
s=''
for x in r:
    s +=x
if s=='':
    print(-1)
else:print(s)