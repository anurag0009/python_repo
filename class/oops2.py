class list_parser:

    def parcer(self,a):
        if type(a) == list:
            for i in a:
                print(i)


    def reverse(self,z):
        if type(z)== list:
            return z[::-1]




a = list_parser()

a.parcer([33,44,55,6,6])
print(a.reverse([33,77,99,88,99]))



# see example 3