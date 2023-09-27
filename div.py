class Div:
  def execute(self, a, b):
    if type(a) == str or type(b) == str:
      return False
    if b == 0:
      return ZeroDivisionError
    else:
      return a / b