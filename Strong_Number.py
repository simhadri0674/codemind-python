def fact(a):
    b=1
    for i in range(1,a+1):
        b *=i
    return b
a=int(input())
b=a
c=0
while b:
    x=b%10
    c +=fact(x)
    b=b//10
if c==a:
    print("The number {} is a strong number".format(a))
else:
     print("The number {} is not a strong number".format(a))
        
        