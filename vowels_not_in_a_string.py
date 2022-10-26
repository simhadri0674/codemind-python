a=input()
c=''
d=[]
for i in a:
    if i in "aeiou":
        c +=i
for j in 'aeiou':
    if j not in c:
        d.append(j)
if d==[]:
    print(0)
else:
    print(*d)
    
        


        