class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
    def get_brand(self):
        return self.__brand + " !"
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "petrol or disel"
    @staticmethod
    def general_description():
        return "cars are means of transport"
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size= battery_size
    def fuel_type(self):
        return "electric charge"


my_car =  Car("toyota","corolla")
print(my_car.get_brand())
print(my_car.full_name())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)

my_tesla = ElectricCar("tesla", "model s","85kwh")
print(my_tesla.full_name())
print(my_tesla.get_brand())
print(my_tesla.total_car)

print(Car.total_car)
print(Car.general_description())

print(my_new_car.model)

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))


class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

my_neww_tesla = ElectricCarTwo("tesla","model x")

print(my_neww_tesla.battery_info())
print(my_neww_tesla.engine_info())