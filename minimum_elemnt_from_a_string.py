a=input()
b=list(a.split(" "))
v=min(b[-1])
c=v.lower()
if c in b[-1]:
    print(c)
else:
    print(v)