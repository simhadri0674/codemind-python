a=int(input())
s=0
for i in range(a):
    b=input()
    if "+" in b:
        s +=1
    else:
        s -=1
print(s)