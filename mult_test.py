import random

from mult import Mult

def test_mult():
  mult = Mult()
  a = random.randint(-1000, 1000)
  b = random.randint(-1000, 1000)

  result = mult.execute(a, b)

  assert result == a * b

def test_mult_type_error():
  mult = Mult()
  a = random.randint(-1000, 1000)
  b = random.randint(-1000, 1000)

  result = mult.execute(str(a), str(b))

  assert result == False