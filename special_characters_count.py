a=input()
b=0
c=0
for i in a:
    if ord(i)>32 and ord(i)<=47:
        c +=1
    elif ord(i)>57 and ord(i)<=64:
        c +=1
    elif ord(i)>91 and ord(i)<=96:
        c +=1
    elif ord(i)>123 and ord(i)<=126:
        c +=1
print(c)
