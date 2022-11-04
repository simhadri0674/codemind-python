a=input()
f=a.lower()
b=0
c=0
d=0
e=0
for i in f:
    if str(i) in "aeiou":
        e+=1
    elif ord(i)>96 and ord(i)<=122:
        b +=1
    elif ord(i)>=47 and  ord(i)<58:
        c +=1
    elif ord(i)==32:
        d+=1
print("Vowels: {}".format(e))
print("Consonants: {}".format(b))
print("Digits: {}".format(c))
print("White spaces: {}".format(d))