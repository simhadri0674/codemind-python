n=int(input())
a=0
b=1
for i in str(n):
    a +=int(i)
    b *=int(i)
if a==b:
    print("Spy Number")
else:
    print("Not Spy Number")