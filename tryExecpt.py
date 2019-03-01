# python中异常处理
try:
  print(5/0)
except ZeroDivisionError as zeroError:
  print(zeroError)
  #pass

print('input 2 number, and I will divide them')
print('Enter q to quit')

while True:
  firstNumber = input('\nFirst Number: ')
  if firstNumber == 'q':
    break
  secondNumber = input('\nSecond Number: ')
  if secondNumber == 'q':
    break
  
  try:
    answer = int(firstNumber) / int(secondNumber)
  except ZeroDivisionError as zeroError:
    print(zeroError)
  else:
    print(answer)
  
# 分析图书
def countWords(filename):
  try:
    with open(filename) as fileObject:
      contents = fileObject.read()
  except FileNotFoundError as fileNotFound:
    print(fileNotFound)
  else:
    words = contents.split()
    numWords = len(words)
    print('The file ' + filename + ' has about ' + str(numWords) + ' words')

fileName = 'pi.txt'
countWords(fileName)