from controller import Robot, Motor, DistanceSensor
<<<<<<< HEAD
from ikpy.chain import Chain
import numpy as np
import time


=======
import time
>>>>>>> origin

robot = Robot()

# initialize motors
mot = []
motNames = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
for name in motNames:
    mot.append(robot.getMotor(name))
<<<<<<< HEAD
   # print("Got " + name)
    
    
#print(robot)  
my_chain = Chain.from_urdf_file("../../ur10.urdf")
#sprint(my_chain.links)

a = np.array([6.0,-0.5,0.0,0.0,0.0,0.0,0.0,7.0])
b = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
z = 0

while 1:
    
    if z == 1:
        i = 1
        while i < 7:
            mot[i -1].setVelocity(0.5)
            mot[i - 1].setPosition(b[i-1])
            i +=1
        
        ret = my_chain.forward_kinematics(b, True)
        
        j = 1
        for item in ret:
            if j == 1:
                print("origin is")
            elif j == 8:
                print("end is")
            else:
                print("joint " + str(j -1 ) + " is ")
            print(item)
            j +=1
        robot.step(16000) 
        z = 0
        
            
    else:
        
        i = 1
        while i < 7:
            mot[i -1].setVelocity(0.5)
            mot[i - 1].setPosition(a[i-1])
            i +=1
        
        ret = my_chain.forward_kinematics(a, True)
        
        j = 1
        for item in ret:
            if j == 1:
                print("origin is")
            elif j == 8:
                print("end is")
            else:
                print("joint " + str(j -1 ) + " is ")
            print(item)
            j +=1
        robot.step(16000) 
        z = 1
        
       
=======
    print("Got " + name)

dir = 0

while(True):
    if dir == 0:
        mot[1].setVelocity(1.5)
        mot[1].setPosition(-3.14)
        dir = 1
    if dir == 1:
        mot[1].setVelocity(1.5)
        mot[1].setPosition(3.14)
        dir = 0

>>>>>>> origin
pass