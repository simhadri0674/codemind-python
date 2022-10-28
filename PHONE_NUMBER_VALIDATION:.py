a=input()
b=len(a)
c=[]
for i in a:
    c.append(i)
if b==10 and int(c[0])>1:
    print("Valid")
else:
    print("Invalid")