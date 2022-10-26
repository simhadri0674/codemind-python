def count(a):
    b=len(a)
    return b

a=input()
b=list(a.split(" "))
c=0
for i in b:
    print(count(i),end=" ")