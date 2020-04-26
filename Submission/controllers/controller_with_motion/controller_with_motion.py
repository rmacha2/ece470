from controller import Robot, Motor, DistanceSensor, Receiver
from ikpy.chain import Chain
import ikpy
import numpy as np
import time

robot = Robot()
receiver = robot.getReceiver('receiver')
receiver.enable(32)
receiver.setChannel(1)

# initialize motors
mot = []
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
                
tempAngles = []

while 1:  
    
    while receiver.getQueueLength() > 0:
        print("Receiver data is")
        data_byte = receiver.getData()
        data_str = data_byte.decode()
        data_list = data_str.split(" ")
        data = [float(data_list[0]),float(data_list[1]),float(data_list[2])]
        
        print(data)
        receiver.nextPacket()