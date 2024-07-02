import random


def is_prime(func):
  def wraper(*args):
    temp_var = func(*args)
    i = random.randint(1, 10)
    if temp_var % 1 == 0 and temp_var % temp_var == 0 and temp_var % i == 0:
      return "Составное число"
    else:
      return "Простое число"
  return wraper
  

@is_prime
def sum_three(*args):
  a = 0
  for var in args:
    a += var
  return a


result = sum_three(2, 3, 6)
print(result)
