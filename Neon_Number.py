n=int(input())
a=n*n
b=0
for i in str(a):
    b +=int(i)
if b==n:
    print("Neon Number")
else:
    print("Not Neon Number")