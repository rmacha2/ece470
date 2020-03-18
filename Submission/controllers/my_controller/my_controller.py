from controller import Robot, Motor, DistanceSensor
import time

robot = Robot()

# initialize motors
mot = []
motNames = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
for name in motNames:
    mot.append(robot.getMotor(name))
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

pass