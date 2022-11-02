a=input()
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
c=d[a[-1]]
for i in range(len(a)-1):
    if d[a[i]]<d[a[i+1]]:
        c-=d[a[i]]
    else:
        c+=d[a[i]]
print(c)