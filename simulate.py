import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np


# connecting to world
physicsClient = p.connect(p.GUI)
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# setting gravity
p.setGravity(0, 0, -9.8)

# setting the floor
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


# loading in box
p.loadSDF("world.sdf")

# additional setting up
pyrosim.Prepare_To_Simulate(robotId)

# vector for storing
backLegSensorValues = np.zeros(100)

# running simulation at specified time lengths
for i in range(100):
    p.stepSimulation()
    time.sleep(1/60)
    #print(i)

    # adding touch sensor
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")

#print(backLegSensorValues)
np.save('data/backLegSensorValues.npy', backLegSensorValues)

# disconnecting from world
p.disconnect()

