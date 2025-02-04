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
    def Act(self, t, robotId):
        for motor in self.motors.values():
            motor.Set_Value(t, robotId)
    def Think(self):
        self.nn.Update()
        self.nn.Print()

