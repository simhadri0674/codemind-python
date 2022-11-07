def bintooct(o):
    c=oct(int(o,2))
    return c
for i in range(int(input())):
    a=input()
    b=bintooct(a)
    print(b[2:])