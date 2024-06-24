main_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def filter_func(in_num):
  return in_num % 2 != 0

def square(value):
  return value ** 2

filtered_list = filter(filter_func, main_list)
result = map(square, filtered_list)

print(list(result))
