a=input()
c=0
s=''
for i in a:
    if int(i)%2!=0:
        c =int(i)*int(i)
        s +=str(c)
        
print(s)
        