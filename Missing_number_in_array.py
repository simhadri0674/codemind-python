for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=[]
    d=[]
    for i in range(1,a+1):
        c.append(i)
    for j in c:
        if j not in b:
            d.append(j)
    print(*d)