def is_prime(func):
  def wraper(*args):
    temp_var = func(*args)
    variants = 0
    for i in range(2, temp_var - 1):
        if temp_var % 1 == 0 and temp_var % temp_var == 0:
            if temp_var % i == 0:
                variants += 1
                
    if variants > 1:
        return f"Составное число\n{temp_var}"
    else:
        return f"Простое число\n{temp_var}"
  return wraper
  

@is_prime
def sum_three(*args):
  a = 0
  for var in args:
    a += var
  return a


result = sum_three(2, 3, 6)
print(result)
