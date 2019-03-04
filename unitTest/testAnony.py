import unittest
from anony import AnonySurvey

class TestAnonySuvery(unittest.TestCase):
  def setUp(self):
    question = 'what language did you first learn to speak?'
    self.mySuvery = AnonySurvey(question)
    self.responses = ['Chinese', 'English', 'Spanish']

  def testStoreSignleRes(self):
    self.mySuvery.storeResponse('Chinese')
    self.assertIn('Chinese', self.mySuvery.responses)

  def testStoreMutilRes(self):
    for response in self.responses:
      self.mySuvery.storeResponse(response)

    for response in self.responses:
      self.assertIn(response, self.mySuvery.responses)

unittest.main()