import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.nn = NEURAL_NETWORK("brain.nndf")

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
                self.motors[jointName].Set_Value(desiredAngle, robotId)
                # print(neuronName, jointName, desiredAngle)
        # for motor in self.motors.values():
        #     motor.Set_Value(desiredAngle, robotId)
    def Think(self):
        self.nn.Update()
        self.nn.Print()
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # writing xCoordinateOfLinkZero to a fitness file
        file = open("fitness.txt", "w")
        file.write(str(xCoordinateOfLinkZero))
        file.close()

