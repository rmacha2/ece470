from controller import Supervisor, Node
from controller import Robot, Motor, DistanceSensor, Emitter
from ikpy.chain import Chain
import ikpy
import numpy as np
import time

TIME_STEP = 32

sup = Supervisor()
emitter = Emitter("emitter")
emitter.setChannel(1)


ball_node = sup.getFromDef("BALL")
trans_field = ball_node.getField("translation")



while sup.step(TIME_STEP) != -1:
    values = trans_field.getSFVec3f()
    supl = str(values[0]) + " " + str(values[1]) + " " + str(values[2]) + " "
    bytes = supl.encode()
    emitter.send(bytes)
    
   # print("Ball is at position: %g %g %g" % (values[0], values[1], values[2]))
    
