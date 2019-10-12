import random

class Event:
  def __init_(self):
    pass

  def happen(self):
    options = random.choices(range(-100, 100), k = random.choice([2,3,4]))
    options = [x/100 for x in options]
    return options

class Subject:
  def __init__(self):
    self.result = 0
  
  def take_action(self, options):
    choice = random.choice(options)
    self.result += choice
    return

life = Event()
human = Subject()
y, z = 0, []

while True:
  options = life.happen()
  human.take_action(options)

  z.extend(options)
  if human.result != 1: # optimal
    y += 1
    print(human.result, y, len(z))
    continue
  else:
    print(y, len(z))
    break