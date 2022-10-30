def pal(a):
    b=a[::-1]
    if a==b:
        return 1
    else:
        return 0
a=input()
b=a.lower()
c=list(b.split(" "))
d=0
for i in c:
    if pal(i):
        d +=1
print(d)
    