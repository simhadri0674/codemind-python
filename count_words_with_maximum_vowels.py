def cou(a):
    c =0
    for j in a:
        if j in "aeiou":
            c +=1
    return c
n=input()
b=list(n.split(" "))
c=[]
for i in b:
    c.append(cou(i))
d=max(c)
e=c.count(d)
print(e)
    