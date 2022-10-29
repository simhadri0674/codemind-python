a=input()
b=0
for i in a:
    if ord(i)>47 and ord(i)<=57:
        b +=1
if b>0:
    print("Contains {} digit".format(b))
else: print("Doesn't contain digit")