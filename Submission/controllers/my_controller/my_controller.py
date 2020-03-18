from controller import Robot, Motor, DistanceSensor
from ikpy.chain import Chain
import numpy as np
import time



robot = Robot()

# initialize motors
mot = []
motNames = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
for name in motNames:
    mot.append(robot.getMotor(name))
   # print("Got " + name)
    
    
#print(robot)  
my_chain = Chain.from_urdf_file("../../ur10.urdf")
#sprint(my_chain.links)

a = np.array([7.0,1.57,0.0,0.0,0.0,0.0,0.0,7.0])
i = 1

while i < 7:
    mot[i -1].setVelocity(0.5)
    mot[i - 1].setPosition(a[i])
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
"""
while 1:
    if robot.step(32) == -1:
        break


a = np.array([7.0,0.0,0.0,0.0,0.0,0.0,0.0,7.0])
i = 1

while i < 7:
    mot[i -1].setVelocity(0.5)
    mot[i - 1].setPosition(a[i])
    i +=1

ret = my_chain.forward_kinematics(a)
print(ret)
"""

pass