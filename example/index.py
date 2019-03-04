import matplotlib.pyplot as plt
from randomWalk import RandomWalk

rw = RandomWalk()
rw.fillWalk()

plt.scatter(rw.xValues, rw.yValues, s = 15)

# points = [1, 2, 4, 6, 7]
# plt.plot(points, linewidth = 5)

# 设置图表样式
# plt.title('Square Numbers', fontSize = 24)
# plt.xlabel('value', fontsize = 18)
# plt.ylabel('square of value', fontsize = 16)

# 设置刻度大小
# plt.tick_params(axis = 'both', labelsize = 14)
plt.show()