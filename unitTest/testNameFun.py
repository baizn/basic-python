# 单元测试
import unittest
from nameFun import getFormattedName

class NameTestCase(unittest.TestCase):
  def testFirstLastName(self):
    formateedName = getFormattedName('b', 'a')
    self.assertEqual(formateedName, 'B A')

  def testMiddleName(self):
    formmatedName = getFormattedName('bai', 'z', 'n')
    self.assertEqual(formmatedName, 'Bai N Z')

unittest.main()