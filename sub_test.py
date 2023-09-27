import random

from sub import Sub

def test_sub():
  sum = Sub()
  a = random.randint(-1000, 1000)
  b = random.randint(-1000, 1000)

  result = sum.execute(a, b)

  assert result == a - b

def test_sub_type_error():
  sub = Sub()
  a = random.randint(-1000, 1000)
  b = random.randint(-1000, 1000)

  result = sub.execute(str(a), str(b))

  assert result == False