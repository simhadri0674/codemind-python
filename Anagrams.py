a=input()
c=a.lower()
b=input()
d=b.lower()
e=0
for i in c:
    if i in d:
        e +=1
print(e==len(a))