a=input()
l=list(a.split(":"))
c=abs(30*float(l[0])-(11/2)*float(l[1]))
d=abs(360-c)
print(min(c,d))