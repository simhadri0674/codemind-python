a=int(input())
b=int(input())
for i in range(1,b+1):
    c,d=map(int,input().split())
    if (c==a and d==a) or (c>a and d>a and c==d):
        print('ACCEPTED')
    elif c<a or d<a:
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")
        