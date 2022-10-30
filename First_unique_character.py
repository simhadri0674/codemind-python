a=input()
d=a.lower()
b=list(d.split(" "))
s=""
for i in b:
    s +=i
f=''
g=0
h=0
for j in s:
    if str(j) not in f:
        f +=str(j)
for k in f:
    if s.count(k)==1:
        g=k
        h=1
        break
if h==0:
    print(-1)
else:
    print(g)
        