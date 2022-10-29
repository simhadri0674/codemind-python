a=input()
c=0
for i in a:
    if ord(i)>47 and ord(i)<=57:
        c +=int(i)
print(c)