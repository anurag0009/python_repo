def even(l):
    enum = []
    for n in l:
        if n%2 ==0:
            enum.append(n)
    return enum




a= [2,4,3,5,6,88]
print(even(a))