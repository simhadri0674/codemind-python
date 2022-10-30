a=input()
d=a.lower()
b=list(d.split(" "))
s=""
for i in b:
    s +=i
f=[]
for j in s:
    if str(j) not in f:
        f.append(j)
g=sorted(f)
h=''
for k in g:
    h +=k
print(h)