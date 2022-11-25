class xyz:
    def __init__(self,a,b,c):
        self.a = a
        self.b =b
        self.c = c

    def test(self):
        print("this is the forst class of test",self.a)
    
    def test1(self):
        print("this is the secod class")

    def test2(self):
        print("this the third class")



inh = xyz(1,2,3)
inh.test()


#inheritence

class xyz1(xyz):
    def test(self):
        print("this is from child class")


q = xyz1(3,4,5)
q.test()