a=input()
b=a.lower()
c=list(b.split(" "))
s=''
for i in c:
    s +=i
f=''
g=''
h=''
for j in  s:
    if str(j) not in f:
        f +=j
for k in f:
    if s.count(k)==1:
        g +=str(k)
l=sorted(g)
for m in l:
    h +=m
print(h)
    