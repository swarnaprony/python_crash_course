#my_car
#date: 12/06/2020

from car import Car
from electric_car import ElectricCar as EC

#import car
"""this approach is not recomended"""




my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_bettle = Car('volkswagen', 'beetle', '2019')
print(my_bettle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', '2019')
print(my_tesla.get_descriptive_name())

#my_bettle = car.Car('volkswagen', 'beetle', '2019')
#print(my_bettle.get_descriptive_name())

#my_tesla = car.ElectricCar('tesla', 'roadster', '2019')
#print(my_tesla.get_descriptive_name())