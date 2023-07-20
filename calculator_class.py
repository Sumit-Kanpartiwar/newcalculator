
class calculator():
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2
  def add(self):
    result = self.num1+self.num2
    return result
  def sub(self):
    result = self.num1-self.num2
    return result
  def prod(self):
    result = self.num1*self.num2
    return result
  def div(self):
    try:
      result = self.num1/self.num2
      return result
    except Exception as e:
      print(f"exception is {e}")
      return "can't divide by zero"
