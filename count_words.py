def count(a):
    c=0
    d=[]
    for i in a:
        d.append(i)
    for j in d:
        if (d[0] in "aeiouAEIOU ") and (d[-1] not in 'aeiouAEIOU'):
            c+=1
    return c
a=input()
b=list(a.split(" "))
c=0
for i in b:
    if count(i):
        c+=1
print(c)
        