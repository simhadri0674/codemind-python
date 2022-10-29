for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    for i in c:
        if i not in d:
            d.append(i)
    e=sorted(d)
    print(*e)