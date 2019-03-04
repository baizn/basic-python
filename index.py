'''
@Author: moyee
@Date: 2019-02-15 12:00:01
@LastEditors: moyee
@LastEditTime: 2019-03-03 16:59:04
@Description: python数字演算
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

number = 7
guess = -1
print('数字猜谜游戏')
while guess != number:
  guess = int(input('请输入数字'))

  if guess == number:
    print('恭喜，你猜对了')
  elif guess < number:
    print('猜的太小了……')
  elif guess > number:
    print('猜的太大了……')

### if case
var1 = 100
if var1:
  print('1 - if true')
  print(var1)

var2 = 0
if var2:
  print('2 - if false')
  print(var2)

print('good bye')

age = int(input('输入年龄'))
print('')
if age < 0:
  print('error input')
elif age == 1:
  print('14')
elif age == 2:
  print('22')
elif age > 2:
  human = 22 + (age - 2) * 5
  print('对应年龄：', human)

### 退出提示
input('点击enter退出')

### while使用
n = 100
sum = 0
counter = 0
while counter <= n:
  sum = sum + counter
  counter += 1
else:
  print('执行over')
print('1到%d之和为： %d' % (n, sum))

### for
sites = ['baidu', 'google', 'alibaba']
for site in sites:
  if site == 'alibaba':
    print('alipay')
    break
  print('data:' + site)
else:
  print('no data')
print('over')

for i in range(len(sites)):
  print(i, sites[i])

# python class
class Restaurant():
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0
  
  def describe_reataurant(self):
    print('name:', self.describe_reataurant)
    print('type:', self.cuisine_type)
    print('server person count:', self.number_served)

  def open_restaurant(self):
    print('open')

  def set_number_served(self, count):
    self.number_served = count

  def increment_number_served(self, num):
    self.number_served += num

restaurant = Restaurant('baizn', 'fe')
restaurant.describe_reataurant()
restaurant.open_restaurant()