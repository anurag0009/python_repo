# class 
class car :
    def __init__(self  , brand_name, fuel_type,body_type):
        self.brand_name = brand_name
        self.fuel_type = fuel_type
        self.body_type = body_type

    def desc_car(self):
        print(self.brand_name,self.fuel_type,self.body_type)


innova = car("toyota","petrol","sedan")
nexon = car('tata',"petrol","suv")
fortuner = car("toyota","diesal","xuv")


innova.desc_car()
print(innova.brand_name)
nexon.desc_car()
print(nexon.body_type)
fortuner.desc_car()
print(fortuner.fuel_type)

