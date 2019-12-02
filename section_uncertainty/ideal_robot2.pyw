#import matplotlib 
#matplotlib.use('nbagg')
import matplotlib.pyplot as plt 
import matplotlib.animation as anm
class World:
    def __init__(self,time_span,time_interval,debug=False):
        self.objects=[]
        self.debug=debug
        self.time_span=time_span
        self.time_interval=time_interval
    def append(self,obj):
        self.objects.append(obj)
    def draw(self):
        fig=plt.figure(figsize=(4,4))
        ax=fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlim(-5,5)
        ax.set_ylim(-5,5)
        ax.set_xlabel("X",fontsize=10)
        ax.set_ylabel("Y",fontsize=10)
        
        elems=[]
        
        if self.debug:
            for i in range(1000):self.one_step(i,elems,ax)
        else:
            self.ani = anm.FuncAnimation(fig,self.one_step,fargs=(elems,ax),frames=10,interval=1000,repeat=False)
        plt.show()
    def one_step(self,i,elems,ax):
        while elems:elems.pop().remove()
        time_str = "t=%.2f(s)" % (self.time_interval*i)
        elems.append(ax.text(-4.4,4.5),time_str,fontsize=10)
        for obj in self.objects:
            obj.draw(ax,elems)
            if hasattr(obj,"one_step"):obj.one_step(self.time_interval)

        
        

import math
import matplotlib.patches as patches 
import numpy  as np

class IdealRobot:
    def __init__(self,pose,color="black"):
        self.pose=pose
        self.r=0.2
        self.color=color
        self.agent=agent
        self.poses=[pose]
    
    def draw(self,ax,elems):
        x,y,theta=self.pose
        xn=x+self.r*math.cos(theta)
        yn=y+self.r*math.sin(theta)
#        ax.plot((x,xn),(y,yn),color=self.color)
        c=patches.Circle(xy=(x,y),radius=self.r,fill=False,color=self.color)
 #       ax.add_patch(c)
        elems+=ax.plot([x,xn],[y,yn],color=self.color)
        elems.append(ax.add_patch(c))

        self.poses.append(self.pose)
        elems+= ax.plot([e[0] for e in self.poses],[e[1] for e in self.poses],linewidth=0.5,color="black")
    def one_step(self,time_interval):
        if not self.agent: return 
        nu,omega = self.agent.decition()
        self.pose  = self.state_transition(nu,omega,time_interval,self.pose)



class Agent:
    def __init__(self,nu,omega):
        self.nu=nu
        self.omega=omega
    
    def decision(self,observation=None):
        return self.nu,omega

#world=World()
#robot1 = IdealRobot(np.array([2,3,math.pi/6]).T)
#robot2 = IdealRobot(np.array([-2,-1,math.pi/5*6]).T,"red")
#world.append(robot1)
#world.append(robot2)
#world.draw()
