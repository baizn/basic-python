from die import Die
import pygal

die = Die()
results = []
for rollNum in range(100):
  result = die.roll()
  results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.sides):
  frequency = results.count(value)
  frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化展示
hist = pygal.Bar()

hist.title = 'Result of rolling on D6 100 times'
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')