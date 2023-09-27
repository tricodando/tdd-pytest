class Sum:
  def execute(self, a, b):
    if type(a) == str or type(b) == str:
      return False
    else:
      return a + b