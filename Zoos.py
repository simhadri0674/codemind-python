a=input()
c=''
for i in a:
    if i not in c:
        c +=i
d=sorted(c)
e=[]
for j in d:
    e.append(a.count(j))
if e[0]==2*(e[1]):
    print("Yes")
else:
    print("No")