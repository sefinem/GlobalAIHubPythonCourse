# Day 5
class Animals():
  def __init__(self, legs, tail):
    self.legs = legs
    self.tail = tail

class Dogs(Animals):
  def sound(self):
    print(f'Huff huff')

class Cats(Animals):
  def sound(self):
    print(f'Meow meow')

cat1 = Cats(4,True)
dog1 = Dogs(4,True)
cat1.sound()
dog1.sound()