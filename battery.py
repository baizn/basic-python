# 定义电瓶
class Battery():
  def __init__(self, batterSize = 70):
    self.batterSize = batterSize

  def descriptionBattery(self):
    print('This car has a ' + str(self.batterSize) + '-kwh battery')

