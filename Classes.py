from mimetypes import init
from os import name
from turtle import update


class Dog:
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} sit")
    def roll(self):
        print(f"{self.name} roll")

my_dog = Dog("rex", 4)
print (f"my dogs name is {my_dog.name}")
print (f"my dogs is aged {my_dog.age}")
my_dog.roll()
my_dog.sit()


#car class
class Car:
    def __init__(self ,name ,model , year ,price):
        self.model = model
        self.name =name
        self.year = year
        self.price =price
        #setting a default value 
        self.odometer =0
    def update_odometer(self ,mileage):
        self.mileage = mileage
        self.odometer = mileage

    def get_car_info(self):
        print (f"the car{self.name} was made in the year {self.year} and costs {self.price}")

my_car = Car('Audi' , 'X5',2009,10000)

#changing default values 
my_car.odometer = 67 #THIS can also be done using a method 
#change mileage using method
my_car.update_odometer(90)

my_car.get_car_info()

#inheritance

class electric_car(Car):
    def __init__(self,name,model,year,price):
        super().__init__(name,model,year,price)

tesla = electric_car('tes', 'A$', 2019,'$10,000')
tesla.get_car_info()

#you can overide a method by using the same name
