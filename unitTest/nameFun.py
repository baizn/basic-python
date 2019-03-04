# format name
def getFormattedName(first, last, middle = ''):
  if middle:
    fullName = first + ' ' + middle + ' ' + last
  else:
    fullName = first + ' ' + last
  return fullName.title()