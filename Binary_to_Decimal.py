for _ in range(int(input())):
    a=input()
    b=a[::-1]
    c=len(b)
    fc=0
    for i in range(c):
        fc +=(2**i)*int(b[i])
    print(fc)