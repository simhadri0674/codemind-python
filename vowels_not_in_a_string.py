a=input()
s=""
x=""
for i in a:
    if i in "aeiou":
        s+=i
for j in "aeiou":
    if j not in s:
        x+=j
if x=="":
    print(0)
else:
    for i in x:
        print(i,end=" ")