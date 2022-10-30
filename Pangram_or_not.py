a=input()
b=a.lower()
c=list(b.split(" "))
d=''
e=''
f=0
for i in c:
    d +=i
for j in d:
    if j not in e:
        e +=j
for k in e:
    if ord(k)>=97 and ord(k)<=122:
        f +=1
print(f==26)
        