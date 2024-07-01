class EvenNumbers:
  def __init__(self, start, end):
    self.start = 0 if start==None else start
    self.end = 1 if end==None else end

  def __iter__(self):
    self.i = 0
    return self

  def __next__(self):
    self.i += 1
    if self.start != self.end:
      if self.start %2 == 0:
        a = self.start
        self.start += 1
        return a
      else:
        self.start += 1
        return self.__next__()
    else:
      raise StopIteration()

en = EvenNumbers(10, 25)
for i in en:
  print(i)
        
  
