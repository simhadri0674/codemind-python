for _ in range(int(input())):
    a=input()
    c=0
    for i in a:
        if ord(i)>47 and ord(i)<=57:
            c +=1
    if c==0:
        print("No")
    else:
        print('Yes')