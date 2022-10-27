for i in range(int(input())):
    n,a,b,k=map(int,input().split())
    if (n//a)>=k or (n//b)>=k:
        print("Win")
    else:
        print("Lose")