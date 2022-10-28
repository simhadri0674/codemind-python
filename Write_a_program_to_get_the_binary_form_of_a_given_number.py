for i in range(int(input())):
    a=int(input())
    c=""
    while 1:
        b=a%2
        c+=str(b)
        a=a//2
        if a==1:
            c +=str(a)
            break
    d=c[::-1]
    print(d)