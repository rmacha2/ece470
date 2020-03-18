from controller import Robot, Motor, DistanceSensor
from ikpy.chain import Chain



robot = Robot()

# initialize motors
mot = []
motNames = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
for name in motNames:
    mot.append(robot.getMotor(name))
    print("Got " + name)
    
    
#print(robot)  
my_chain = Chain.from_urdf_file("../../ur10.urdf")
print(my_chain.links)


pass