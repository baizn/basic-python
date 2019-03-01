# 描述一辆car
class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometerReading = 0
  
  def getDescriptionName(self):
    longName = str(self.year) + ' ' + self.make + ' ' + self.model
    return longName.title()

  def readOdometer(self):
    print('the car has ' + str(self.odometerReading) + ' miles on it.')

  def updateOdometer(self, mileage):
    if mileage >= self.odometerReading:
      self.odometerReading = mileage
    else:
      print('you can not roll back an odometer.')

  def increment(self, miles):
    self.odometerReading += miles