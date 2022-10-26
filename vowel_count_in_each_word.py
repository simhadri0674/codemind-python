def count(a):
    c=0
    for i in a:
        if i in "aeiouAEIOU":
            c +=1
    return c
a=input()
b=list(a.split(" "))
for i in b:
    print(count(i),end=" ")
