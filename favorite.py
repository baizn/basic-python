from collections import OrderedDict
from random import randint

favoriteLanguage = OrderedDict()
favoriteLanguage['baizn'] = 'python'
favoriteLanguage['zhan'] = 'javascript'
favoriteLanguage['ning'] = 'node'

for name, language in favoriteLanguage.items():
  print(name.title() + "'s favorite languang is " + language.title())


class Die():
  def __init__(self, sides = 6):
    self.sides = sides

  def rollDie(self):
    for i in range(5):
      print(self.sides, randint(1, self.sides))
      
die = Die()
die.rollDie()

die10 = Die(20)
die10.rollDie()