a=input()
b=a.lower()
c=list(b.split(" "))
s=''
for i in c:
    s +=i
f=''
g=h=0
for j in  s:
    if str(j) not in f:
        f +=j
for k in f:
    if s.count(k)==1:
        h +=1
print(h)