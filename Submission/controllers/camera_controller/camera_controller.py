from controller import Robot, Motor, DistanceSensor
from ikpy.chain import Chain
import numpy as np
import time
from controller import Camera, Device

robot = Robot()

camera = Camera("camera")

camera.enable(20)