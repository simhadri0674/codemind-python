a=input()
c=len(a)
b=input()
for i in range(c):
    if a[i]==b:
        break
if b in a:
    print("True")
    print(i)
else:
    print("False")