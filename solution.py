import random
import time

import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import constants as c
class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        self.fitness = 0
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        # Create barriers on both sides of the runway
        pyrosim.Send_Cube(name="LeftBarrier", pos=[-5, 5, 1], size=[0.2, 15, 2])  # Left wall
        pyrosim.Send_Cube(name="RightBarrier", pos=[5, 5, 1], size=[0.2, 15, 2])  # Right wall

        # Place four pillars as obstacles on the runway
        pyrosim.Send_Cube(name="Pillar1", pos=[-1.5, 2, 0.75], size=[0.3, 0.3, 1.5])  # First pillar
        pyrosim.Send_Cube(name="Pillar2", pos=[0, 4, 0.75], size=[0.3, 0.3, 1.5])  # Second pillar
        pyrosim.Send_Cube(name="Pillar3", pos=[0, 8, 0.75], size=[0.3, 0.3, 1.5])  # Third pillar
        pyrosim.Send_Cube(name="Pillar4", pos=[3, 10, 0.75], size=[0.3, 0.3, 1.5])  # Fourth pillar


        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # assigning torso variables
        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1],jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1],jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.5], size=[0.2, 0.2, 1])
        pyrosim.End()

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Start_NeuralNetwork(f"brain{str(self.myID)}.nndf")

        # generating neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg")

        # motor nurons
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg_RightLowerLeg")

        # generating synapses
        # fully connected neural network
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 6,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 simulate.py {directOrGUI} {str(self.myID)} 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness{str(self.myID)}.txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        file = open(fitnessFileName, "r")
        self.fitness = float(file.read())
        file.close()
        os.system(f"rm {fitnessFileName}")
        # print(f"fitness {str(self.myID)}:", self.fitness)


    def Mutate(self):
        # select a random row/sensor neuron
        randomRow = random.randint(0,  c.numSensorNeurons - 1)

        # select a random column/motor neuron
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
    def Set_ID(self, newID):
        self.myID = newID
