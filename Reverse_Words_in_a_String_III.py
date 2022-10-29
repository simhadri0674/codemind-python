def rev(a):
    b=a[::-1]
    return b
a=input()
b=list(a.split(" "))
c=[]
for i in b:
    print(rev(i),end=" ")
