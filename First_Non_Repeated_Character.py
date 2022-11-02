for _ in range(int(input())):
    a=int(input())
    b=input()
    c=0
    d=[]
    for i in b:
        if b.count(i)==1:
            d.append(i)
    if d==[]:
        print(-1)
    else:
        print(d[0])
    