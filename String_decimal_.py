for _ in range(int(input())):
    a=input()
    c=0
    for i in a:
        if ord(i)>47 and ord(i)<58:
            c +=1
    d=len(a)
    print(d==c)