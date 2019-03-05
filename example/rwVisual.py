# 模拟多次
import matplotlib.pyplot as plt
from randomWalk import RandomWalk

while True:
  rw = RandomWalk(50000)
  rw.fillWalk()

  # 设置绘图窗口的尺寸
  plt.figure(figsize = (10, 6))

  # 设置样式
  pointNumbers = list(range(rw.points))
  plt.scatter(rw.xValues, rw.yValues, 
    c = pointNumbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)

  # 突出起点和终点
  plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
  plt.scatter(rw.xValues[-1], rw.yValues[-1], 
    c = 'red', cmap = plt.cm.Blues, edgecolors = 'none', s = 100)

  # 隐藏坐标轴
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)

  plt.show()

  keepRunnding = input('Make another walk? (y/n)')
  if keepRunnding == 'n':
    break