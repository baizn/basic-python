# 骰子类
from random import randint

class Die():
  def __init__(self, sides = 6):
    self.sides = sides

  def roll(self):
    # 返回1-sides之间的数值
    return randint(1, self.sides)