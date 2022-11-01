a=int(input())
d={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K"}
for i in range(a,0,-1):
    for j in range(1,i+1):
        print(d[i],end=" ")
    print()