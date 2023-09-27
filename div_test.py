import random

from div import Div

def test_div():
  div = Div()
  a = random.randint(-1000, 1000)
  b = random.randint(1, 1000)

  result = div.execute(a, b)

  assert result == a / b

def test_div_zero_division_error():
  div = Div()
  a = random.randint(-1000, 1000)
  b = 0

  result = div.execute(a, b)

  assert result == ZeroDivisionError

def test_div_type_error():
  div = Div()
  a = random.randint(-1000, 1000)
  b = random.randint(1, 1000)

  result = div.execute(str(a), str(b))

  assert result == False