a=input()
b=a.lower()
c=0
for i in range(len(a)):
    if a.count(a[i])==1:
        print(i)
        c +=1
        break
if c==0:
    print(-1)
        