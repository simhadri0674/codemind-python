a=input()
c=0
d=[]
for i in a:
    if i in "aeiouAEIOU":
        d.append(i)
        c +=1
e=[]
for i in d:
    if i not in e:
        e.append(i)
    
if c==0:
    print("-1")
else:
    print(*e)