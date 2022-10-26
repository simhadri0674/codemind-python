def count(a):
    c=a[::-1]
    return c
a=input()
b=list(a.split(" "))
c=[]
for i in b:
    j=count(i)
    c.append(j)
print(*c)