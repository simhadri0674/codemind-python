def count(a):
    b=len(a)
    return b
a=input()
b=list(a.split(" "))
c=[]
for i in b:
    j=count(i)
    c.append(j)
print(max(c))