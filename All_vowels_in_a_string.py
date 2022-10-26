a=input()
b=list(a.split(" "))
f=''
c=0
d=[]
for j in b:
    f +=str(j)
for i in f:
    if i in "aeiou":
        d.append(i)
        c +=1
e=[]
for i in d:
    if i not in e:
        e.append(i)
print(len(e)==5)