import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
class ROBOT:

    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")

        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system(f"rm brain{solutionID}.nndf")


    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            # # prints sensor names
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            # # prints joint names
            # print(jointName)
            self.motors[jointName] = MOTOR(jointName)
    def Act(self, desiredAngle, robotId):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                desiredAngle = desiredAngle * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, robotId)
                # print(neuronName, jointName, desiredAngle)
        # for motor in self.motors.values():
        #     motor.Set_Value(desiredAngle, robotId)
    def Think(self):
        self.nn.Update()
        self.nn.Print()
    def Get_Fitness(self, solutionID):

        # original code
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        filename = f"tmp{solutionID}.txt"
        file = open(filename, "w")
        # Write the final x-coordinate of link zero
        file.write(str(xPosition))
        file.close()
        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")

