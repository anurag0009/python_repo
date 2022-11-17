l = [1,2,3,4,5,6,"Anurag",10.5]
for i in l:
    print(i)
    print(type(i))


for i in l:
    if type(i) == int:
        print(i)


for i,j in enumerate(l):
    print(i,j)


for i in l:
    if type(i) == str :
        l1 = []
        for j in i:
            l1.append(j)
        print(l1)


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print('anurag', end =" ")
    print("\n")