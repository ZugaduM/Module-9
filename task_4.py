def all_variants(text, a=0):
  if a == 0:
    for variant in text:
      yield variant
    a += 1
  if a == 1:
    for i in range(0, len(text) - 1, 1):
      yield text[i] + text[i + 1]
    a += 1
  if a == 2:
    yield text
      
      

a = all_variants("abc")
for i in a:
  print(i)
