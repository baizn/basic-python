from car import Car
from battery import Battery

class ElectricCar(Car):
  def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery(60)

  # def descriptionBattery(self):
  #   print('This car has a ' + str(self.battery.) + '-km battery')

car = Car('china', 'ds', 2018)
name = car.getDescriptionName()
print(name)
car.readOdometer()
car.updateOdometer(20)
car.readOdometer()

electricCar = ElectricCar('china', 'masldi', 2019)
electricCar.battery.descriptionBattery()

