a=input()
b=list(a.split(" "))
c=[]
c[:]=b[:]
i=0
j=len(b)-1
while i<=j:
    c[i],c[j]=c[j],c[i]
    i +=1
    j -=1
print(*c)