a=input()
b=list(a.split(" "))
c=0
for i in a:
    if a.count(i)==1:
        c +=1
print(c==len(a))