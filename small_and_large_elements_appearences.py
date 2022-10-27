a=input()
b=list(a.split(" "))
s=""
for i in b:
    s +=i
c=min(s)
d=max(s)
print(c,s.count(c),end=" ")
print(d,s.count(d),end=" ")