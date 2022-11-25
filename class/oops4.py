class dict_parcer:

    def dict_key(self , d):
        for i in d.keys():
            print(i)
    
    def dict_key(self , d):
        for i in d.values():
            print(i)

    def dict_check(self,d):
        if(type(d) != dict) :
            print("it is not dictonary")
    
    def dict_in(self, d ,a =int(input())):
        print(d[a])

    def dict_in(self,d,key,value):
        d[key]=value



dictc = dict_parcer()

dictc.dict_key({"a" : "anurag"})
dictc.dict_check(5)