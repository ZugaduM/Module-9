side_a = 2
side_b = 4

class Rect():
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __call__(self):
    return self.a * self.b


def create_operation(operation):
  if operation == "add":
      def add(x, y):
          return x + y
      return add
  elif operation == "subtract":
      def subtract(x, y):
          return x - y
      return subtract
  elif operation == "division":
    def division(x, y):
      return x / y
    return division


my_func_add = create_operation("add")
print(my_func_add(4,2))
my_func_div = create_operation("division")
print(my_func_div(4,2))
try:
  print(my_func_div(4,0))
except ZeroDivisionError:
  print("Error: Division by zero")


multiply = lambda x, y: x * y
print(multiply(2, 8))
print(multiply(4, 4))


my_square = Rect(side_a, side_b)
print(f'Стороны: {side_a}, {side_b}')
print(f'Площадь: {my_square()}')
