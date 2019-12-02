import sys
sys.path.append("../scripts/")
from ideal_robot import *

class Robot(idealRobot):
    pass

word=World(30,0.1)

for i in range(100):
    circling=Agent(0.2,10.0/180*math.pi)
    r=Robot(np.array([0,0,0]).T,sensor=None,agent=circling)
    world.append(r)

world.draw()

from scipy.stats import expon,norm

