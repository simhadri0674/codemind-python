import math 
n= int(input())
l=pow(2,math.floor(math.log(n,2)))
r=l*2
print(min((n-l),(r-n)))