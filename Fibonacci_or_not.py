def fab(a):
    b=0
    c=1
    d=[]
    for i in range(1,a):
        e=b+c
        b=c
        c=e
        d.append(e)
    if a in d:
        return 1
    else:
        return 0
a=int(input())
if fab(a):
    print("True")
else:
    print("False")
        