from controller import Robot, Motor, DistanceSensor
from ikpy.chain import Chain
import numpy as np
import time
from controller import Camera, Device, CameraRecognitionObject

robot = Robot()

camera = Camera("camera")

camera.enable(20)

#firstObject = Camera.getRecognitionObjects()[0]
#id = firstObject.get_id()
#position = firstObject.get_position()