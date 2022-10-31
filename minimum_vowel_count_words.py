def cou(a):
    c=0
    for j in a:
        if j in "aeiou":
            c +=1
    return c
a=input()
b=list(a.split(" "))
c=[]
for i in b:
    c.append(cou(i))
d=min(c)
e=c.count(d)
print(e)