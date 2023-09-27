import random

from sum import Sum

def test_sum():
  sum = Sum()
  a = random.randint(-1000, 1000)
  b = random.randint(-1000, 1000)

  result = sum.execute(a, b)

  assert result == a + b

def test_sum_type_error():
  sum = Sum()
  a = random.randint(-1000, 1000)
  b = random.randint(-1000, 1000)

  result = sum.execute(str(a), str(b))

  assert result == False