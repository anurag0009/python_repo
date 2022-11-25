class abc:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def test(self):
        print("this is the class from xyz")


class xzy:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def test1(self):
        print("this is the class of xyz")



class child(abc,xzy):
    def __init__(self,*awrgs,**kwrgs):
        abc.__init__(self,*awrgs)
        xzy.__init__(self,*kwrgs)



ab= child(1,2,3,p=2,q=6,r=8)

print(ab.y)


