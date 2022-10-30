a=input()
x=a.lower()
b=input()
y=b.lower()
c=list(x.split(" "))
d=list(y.split(" "))
e=[]
for i in d:
    if i in c:
        e.append(i)
print(*e)