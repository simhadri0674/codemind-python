a=int(input())
l=[]
while a:
    r =a%10
    l.append(r)
    a=a//10
l=l[::-1]
for i in range(len(l)):
    if l[i]==6:
        l[i]=9
        break
s=""
for i in l:
    s +=str(i)
print(int(s))