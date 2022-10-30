a=input()
b=list(a.split(" "))
i=0
j=len(b)-1
while i<=j:
    b[i],b[j]=b[j],b[i]
    i +=1
    j -=1
print(*b)
