p,r,t=map(int,input().split())
d=p*(1+(r/100))**t
print("{:.2f}".format(d))
