from random import choice
class RandomWalk():
  def __init__(self, points = 5000):
    self.points = points
    self.xValues = [0]
    self.yValues = [0]

  def fillWalk(self):
    while len(self.xValues) < self.points:
      xDirection = choice([1, -1])
      xDistance = choice([0, 1, 2, 3, 4])
      xStep = xDirection * xDistance

      yDirection = choice([1, -1])
      yDistance = choice([0, 1, 2, 3, 4])
      yStep = yDirection * yDistance

      if xStep == 0 and yStep == 0:
        continue
      
      # 计算下一个点的位置
      nextX = self.xValues[-1] + xStep
      nextY = self.yValues[-1] + yStep

      self.xValues.append(nextX)
      self.yValues.append(nextY)