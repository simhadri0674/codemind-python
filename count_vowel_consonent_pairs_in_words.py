def fun(a):
    b=str(a)
    i=0
    c=0
    j=len(b)-1
    while i<=j:
        if b[i] in "aeiou" and b[j] not in "aeiou":
            c +=1
        elif b[i] not in "aeiou" and b[j] in "aeiou":
            c +=1
        i +=1
        j -=1
    return c
a=input()
c=a.lower()
b=list(c.split())
c=0
for i in b:
    c +=fun(i)
print(c)