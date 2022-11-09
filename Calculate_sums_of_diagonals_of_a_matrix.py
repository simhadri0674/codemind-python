
a=int(input())
l=[]
for i in range(a):
    k=list(map(int,input().split()))
    l.append(k)
c=0
d=l[::-1]
e=0
for i in range(a):
    for j in range(a):
        if i==j:
            c +=l[i][j]
for m in range(a):
    for n in range(a):
        if m==n:
            e +=d[m][n]
print("Principal Diagonal:{}".format(int(c)))
print("Secondary Diagonal:{}".format(int(e)))