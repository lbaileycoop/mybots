from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import math

class SIMULATION:

    def __init__(self):
        # connecting to world
        self.physicsClient = p.connect(p.GUI)
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # setting gravity
        p.setGravity(0, 0, -9.8)

        # creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.world = WORLD()
        self.robot = ROBOT()
        self.robotId = self.robot.robotId

        # additional setting up
        pyrosim.Prepare_To_Simulate(self.robotId)

    def Run(self):
        # vector for storing
        backLegSensorValues = np.zeros(1000)
        frontLegSensorValues = np.zeros(1000)
        backLegTargetAngles = np.zeros(1000)
        frontLegTargetAngles = np.zeros(1000)

        backLegAmplitude = np.pi / 4
        backLegFrequency = 0.1
        backLegPhaseOffset = np.pi

        frontLegAmplitude = np.pi / 4
        frontLegFrequency = 0.1
        frontLegPhaseOffset = np.pi

        # running simulation at specified time lengths
        for i in range(1000):
            p.stepSimulation()
            time.sleep(1 / 240)
            print(i)
            #
            # # adding touch sensors
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #
            # # compute the target angle using amplitude, frequency, and phase offset
            # backLegTargetAngles[i] = backLegAmplitude * math.sin(backLegFrequency * i + backLegPhaseOffset)
            # frontLegTargetAngles[i] = frontLegAmplitude * math.sin(frontLegFrequency * i + frontLegPhaseOffset)
            #
            # # simulating a motor that supplies force to one of the robot's joints
            # # bodyIndex tells the simulator that we are about to simulate a motor in the robot called robotId
            # pyrosim.Set_Motor_For_Joint(bodyIndex=self.robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL,
            #                             targetPosition=backLegTargetAngles[i], maxForce=50)
            #
            # pyrosim.Set_Motor_For_Joint(bodyIndex=self.robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
            #                             targetPosition=frontLegTargetAngles[i], maxForce=50)

    def __del__(self):
        p.disconnect()