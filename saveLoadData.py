# 使用json存储和加载数据

import json
numbers = [2, 3, 4, 5, 6]

fileName = 'number.json'
with open(fileName, 'w') as fileObj:
  json.dump(numbers, fileObj)

with open(fileName, 'r') as fileObj:
  numbers = json.load(fileObj)

print(numbers)

fileName = 'usename.json'
try:
  with open(fileName) as fileObj:
    username = json.load(fileObj)
except FileNotFoundError as fileNotFound:
  username = input('What is your name?')
  with open(fileName, 'w') as fileObj:
    json.dump(username, fileObj)
    print('we will remember you when you com back, ' + username + ' !')
else:
  print('welcome back ' + username + ' !')

'''
获取存储的用户名
'''
def getStoredUserName():
  fileName = 'username.json'
  try:
    with open(fileName, 'r') as fileObj:
      username = json.read(fileObj)
  except FileNotFoundError:
    return None
  else:
    return username

'''
获取新输入的用户名，并保存到文件中
'''
def getNewUserName():
  username = input('what is your name? \n')
  fileName = 'username.json'
  with open(fileName, 'w') as fileObj:
    json.dump(username, fileObj)
  return username

def greetUser():
  username = getStoredUserName()
  if username:
    print('Welcome to back ' + username)
  else:
    username = getStoredUserName()
    print('We will remember you when you come back ' + username + ' !')