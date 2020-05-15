from controller import Robot, Motor, DistanceSensor, Receiver
from ikpy.chain import Chain
import ikpy
import numpy as np
import time

robot = Robot()
robot.step(100)
receiver = robot.getReceiver('receiver')
receiver.enable(32)
receiver.setChannel(1)

# initialize motors
mot = []
angles = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
motNames = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
for name in motNames:
    mot.append(robot.getMotor(name))
   # print("Got " + name)
    
#print(robot)  
my_chain = Chain.from_urdf_file("../../ur10.urdf")
#sprint(my_chain.links)

a = np.array([6.0,-0.5,0.0,0.0,0.0,0.0,0.0,7.0])
b = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

temo = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
z = 1

T1 = np.array([[0.0,0.0,0.0,1.5],\
                [0.0,0.0,0.0,1.0],\
                [0.0,0.0,0.0,2.0],\
                [0.0,0.0,0.0,1.0]])
               
robot.step(100)
print("prgm started")
angles = np.zeros(8)
while 1:  
    data = np.empty(3)
    robot.step(100)
    while receiver.getQueueLength()>0:
        data_byte = receiver.getData()
        data_str = data_byte.decode()
        data_list = data_str.split(" ")
        data = [-1 * (float(data_list[0])-4.26),float(data_list[1]),float(data_list[2])]
        
       # print(data)
        receiver.nextPacket()   
    print("Receiver data is")
    actual_data = [-1 * data[2],data[0], data[1]]
    print(actual_data) 
            
            
    target_frame = np.eye(4)
    target_frame[:3, 3] = actual_data
    inv = ikpy.inverse_kinematics.inverse_kinematic_optimization(my_chain,target_frame,angles)
        
    
    print("inv is ", inv)
            
    
    i = 1
    while i < 7:
        mot[i-1].setVelocity(1)
        if i == 1 or i == 3:
            mot[i-1].setPosition(inv[i])
        else:
            mot[i-1].setPosition(inv[i])
              
        i +=1
        
    robot.step(200)
    i = 0
    while i < 8:
        angles[i] = inv[i]
        i +=1
    
