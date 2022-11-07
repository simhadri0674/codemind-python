def octto(o):
    c=bin(int(o,8))
    return c
for i in range(int(input())):
    o=input()
    b=octto(o)
    print(b[2:])