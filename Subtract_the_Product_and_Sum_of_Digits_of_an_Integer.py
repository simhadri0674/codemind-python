n=int(input())
a=1
b=0
for i in str(n):
    a *=int(i)
    b +=int(i)
print(a-b)