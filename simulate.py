import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import math
import constants as c
from simulation import SIMULATION

# connecting to simulation class
simulation = SIMULATION()

# Call the Run method to start the simulation
simulation.Run()


# connecting to world
# physicsClient = p.connect(p.GUI)
# #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
#
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# # setting gravity
# p.setGravity(0, 0, -9.8)
#
# # setting the floor
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
#
#
# # loading in box
# p.loadSDF("world.sdf")
#
# # additional setting up
# pyrosim.Prepare_To_Simulate(robotId)

# # vector for storing
# backLegSensorValues = np.zeros(1000)
# frontLegSensorValues = np.zeros(1000)
# backLegTargetAngles = np.zeros(1000)
# frontLegTargetAngles = np.zeros(1000)
#
#
# backLegAmplitude = np.pi/4
# backLegFrequency = 0.1
# backLegPhaseOffset = np.pi
#
# frontLegAmplitude = np.pi/4
# frontLegFrequency = 0.1
# frontLegPhaseOffset = np.pi
#
# # running simulation at specified time lengths
# for i in range(1000):
#     p.stepSimulation()
#     time.sleep(1/240)
#     #print(i)
#
#     # adding touch sensors
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
#     # compute the target angle using amplitude, frequency, and phase offset
#     backLegTargetAngles[i] = backLegAmplitude * math.sin(backLegFrequency * i + backLegPhaseOffset)
#     frontLegTargetAngles[i] = frontLegAmplitude * math.sin(frontLegFrequency * i + frontLegPhaseOffset)
#
#
#     # simulating a motor that supplies force to one of the robot's joints
#     # bodyIndex tells the simulator that we are about to simulate a motor in the robot called robotId
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL,
#                                 targetPosition=backLegTargetAngles[i], maxForce=50)
#
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
#                                 targetPosition=frontLegTargetAngles[i], maxForce=50)


#print(backLegSensorValues)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

np.save('data/backLegTargetAngles.npy', backLegTargetAngles)
np.save('data/frontLegTargetAngles.npy', frontLegTargetAngles)

# # disconnecting from world
# p.disconnect()

