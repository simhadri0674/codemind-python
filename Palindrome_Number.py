for i in range(int(input())):
    a=int(input())
    b=a
    c=0
    while a>0:
        r=a%10
        c=c*10+r
        a=a//10
    if b==c:
        print("True")
    else:
        print("False")