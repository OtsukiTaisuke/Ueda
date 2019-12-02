import numpy as np
from copy import copy
import math, random
import matplotlib.pyplot as plt                   #   for plotting data
from matplotlib.patches import Ellipse      #  for drawing

### 変数 ###

# 実際の世界のシミュレーション
actual_x = np.array([0.0,0.0,0.0])   #ロボットの実際の姿勢
u = np.array([0.2,math.pi / 180.0 * 0]) #ロボットの移動

# モンテカルロ法のための変数
class Particle:
    def __init__(self,w):
        self.pose = np.array([0.0,0.0,0.0])
        self.weight = w

    def __repr__(self):
        return "pose: " + str(self.pose) + " weight: " + str(self.weight)
particles = [Particle(1.0/100) for i in range(100)]
# 一個プリントしてみましょう
#print(particles)

def f_kakuritu(x_old,u):
    pos_x, pos_y, pos_theta = x_old
    act_fw, act_rot = u

    #act_fw = random.gauss(act_fw,act_fw/10)
    #dir_error = random.gauss(0.0, math.pi / 180.0 * 3.0)
    #act_rot = random.gauss(act_rot,act_rot/10)
    
    x_act_fw_error = random.gauss(-1.6698,9.18155)
    y_act_fw_error = random.gauss(-1.64,25.8597)
    dir_error = 0#random.gauss(0.0, math.pi / 180.0 * 3.0)
    act_rot_error = random.gauss(-0.1901*math.pi/180,2.79042*math.pi/180)

    pos_x += (act_fw * math.cos(pos_theta + dir_error))+x_act_fw_error
    pos_y += (act_fw * math.sin(pos_theta + dir_error))+y_act_fw_error
 
    pos_theta += act_rot+act_rot_error

    return np.array([pos_x,pos_y,pos_theta])


import copy
path = [actual_x]
particle_path = [copy.deepcopy(particles)]
for i in range(10):
    actual_x = f_kakuritu(actual_x,u)
    path.append(actual_x)
    
    for p in particles:
        p.pose = f_kakuritu(p.pose,u)
    particle_path.append(copy.deepcopy(particles))


#print(path[0])
#print(particle_path[0])
#print(path[10])
#print(particle_path[10])
from matplotlib import animation
def draw(pose,particles):
    fig = plt.figure(i,figsize=(8, 8))
    sp = fig.add_subplot(111, aspect='equal')
    sp.set_xlim(-1000.0,1000.0)
    sp.set_ylim(-500,500)

    xs = [e.pose[0] for e in particles]
    ys = [e.pose[1] for e in particles]
    vxs = [math.cos(e.pose[2]) for e in particles]
    vys = [math.sin(e.pose[2]) for e in particles]
    plt.quiver(xs,ys,vxs,vys,color="blue",label="particles")

    plt.quiver([pose[0]],[pose[1]],[math.cos(pose[2])],[math.sin(pose[2])],color="red",label="actual robot motion")
    print("*****")
    #plt.show(block=False)

for i,p in enumerate(path):
    draw(path[i],particle_path[i])



def main():
    # 描画領域
    # 描画するデータ (最初は空っぽ)

    # グラフを表示する
    plt.show()

main()
