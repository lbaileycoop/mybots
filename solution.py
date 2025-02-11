import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import os
class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        # assigning torso variables
        length = 1
        width = 1
        height = 1
        x = -2
        y = 2
        z = 0.5

        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        # ending program
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # assigning torso variables
        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

        # ending program
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # generating neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # generating synapses
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-100.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-100.0)
        # pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=4, weight=10.0)
        # pyrosim.Send_Synapse(sourceNeuronName=4, targetNeuronName=4, weight=10.0)

        # fully connected neural network
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        # ending program
        pyrosim.End()

    def Evaluate(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 simulate.py {mode}")
        file = open("fitness.txt", "r")
        self.fitness = float(file.read())
        file.close()

    def Mutate(self):
        # select a random row/sensor neuron
        randomRow = random.randint(0, 2)

        # select a random column/motor neuron
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1