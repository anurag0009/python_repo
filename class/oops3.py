class list_parcer:
    def __init__(self,l):
        self.l=l
    
    def parcer(self):
        if type(self.l) == list:
            for i in self.l:
                print(i)


    def reverse(self):
        if type(self.l)== list:
            return self.l[::-1]




a = list_parcer([1,2,3,4,5,6])

a.parcer()
print(a.reverse( ))