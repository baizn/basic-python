# 准备测试的class
class AnonySurvey():
  def __init__(self, question):
    self.question = question
    self.responses = []

  def showQuestion(self):
    print(self.question)

  def storeResponse(self, res):
    self.responses.append(res)

  def showResult(self):
    print('Survery Result:')
    for response in self.responses:
      print('- ' + response)
