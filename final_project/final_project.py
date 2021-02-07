# final project

class Employees():
  languages = set()
  employees = {}

  def __init__(self, name, a, l):
    self.employees[name] = {'age': a, 'language': l}
    if type(l) is list:
      for x in l:
        self.languages.add(x)
    else:
      self.languages.add(l)

  def speak(self):
    print(f"Languages that any employees can speak {', '.join(self.languages)}")

class Manager(Employees):
  pass

emp1 = Employees('a',23,['english','dutch','swahili','malay','arabic','indonesian'])
emp2 = Employees('b',40,['arabic','chinese','japanese','korean','french','italian','english','turkish'])
emp2.speak()