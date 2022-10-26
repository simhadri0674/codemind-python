def count(a):
    c=0
    for i in a:
        if i in "aeiouAEIOU":
            c +=1
    return c
a=input()
b=list(a.split(" "))
c=[]
for i in b:
    j=count(i)
    c.append(j)
print(max(c))