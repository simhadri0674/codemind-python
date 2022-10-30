a=input()
x=a.lower()
b=input()
y=b.lower()
c=list(x.split(" "))
d=list(y.split(" "))
s=''
for i in c:
    s +=i
f=''
g=''
h=''
q=0
for j in  s:
    if str(j) not in f:
        f +=j
for i in d:
    g +=i
for m in g:
    if str(m) not in h:
        h +=m
for n in f:
    if n in h:
        q +=1
print(q)