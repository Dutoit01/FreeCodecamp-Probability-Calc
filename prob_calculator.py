import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)
    
  def draw(self, drawnum):
    balls = [] #will store the drawn balls
    numball=len(self.contents) #let's me lower the index range as I draw
    if drawnum <= len(self.contents):
      for i in range(drawnum):
        ind = random.randint(0, numball-1)
        balls.append(self.contents.pop(ind)) #removes ball from contents and adds it to balls
        numball = numball - 1 
      return balls
    else:
      balls = self.contents
      return balls
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  N = num_experiments
  M = 0 #will count the number of successful experiments
  for i in range(num_experiments):
    thehat = copy.deepcopy(hat)
    balls = thehat.draw(num_balls_drawn)
    tick=0
    count=0 #I'll compare the number of time we have at least as many as the expected ball type with the number of types. If they are equal, we have a success. count counts indiv successes, and tick count ball types
    for k,v in expected_balls.items():
      tick = tick + 1
      if balls.count(k) >= v:
        count = count + 1
    if count == tick:
        M = M + 1
  return M/N


