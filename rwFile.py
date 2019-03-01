# python read file
with open('pi.txt') as fileObject:
  contents = fileObject.read()
  print(contents.rstrip())
  print(len(contents.split()))

# 逐行读取文件
with open('pi.txt') as fileObject:
  for line in fileObject:
    print(line.rstrip())

with open('pi.txt') as fileObject:
  lines = fileObject.readlines()
print('**********')
print(lines)

piStr = ''
replaceStr = 'baizn'
for line in lines:
  if 'python' in line:
    piStr += line.strip().replace('python', replaceStr)
  else:
    piStr += line.strip()
print(piStr)
print(len(piStr))

# write file model: 
# r: readonly;
# w: wirte, clear file content;
# a: append.
with open('pi.txt', 'a') as fileObject:
  fileObject.write('\n made in china')
