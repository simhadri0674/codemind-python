for _ in range(int(input())):
    a=input()
    b=a[::-1]
    c=len(b)
    if a==b and c%2==0:
        print("YES EVEN")
    elif a==b and c%2!=0:
        print("YES ODD")
    else:
        print("NO")
        
        