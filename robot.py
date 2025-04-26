import math
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


        # Define the goal position (the position of the goal block)
        self.goalPosition = [0, 19, 0.5]
        # Track collisions
        self.collision_penalty = 0  # Accumulate penalty for collisions


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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                desiredAngle = max(min(desiredAngle, c.motorJointRange), -c.motorJointRange)
                self.motors[jointName].Set_Value(desiredAngle, robotId)
    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Check_Collisions(self):
        static_obs = {"LeftBarrier", "RightBarrier", "BackWall"}

        for body_id in range(p.getNumBodies()):
            name = p.getBodyInfo(body_id)[1].decode("utf-8")
            if name in static_obs or name.startswith("Obstacles"):
                if p.getContactPoints(self.robotId, body_id):
                    self.collision_penalty += 10
    def Get_Fitness(self, solutionID):
        # Get the base position of the robot
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]
        zPosition = basePosition[2]

        # Define the goal position
        goal_x, goal_y, goal_z = self.goalPosition

        # Calculate Euclidean distance to the goal
        distance_to_goal = math.sqrt((xPosition - goal_x) ** 2 + (yPosition - goal_y) ** 2 + (zPosition - goal_z) ** 2)

        # Define maximum possible distance
        max_distance = math.sqrt((7 ** 2) + (19 ** 2) + (1 ** 2))

        # Base fitness is Higher when closer to goal
        fitness = 1 - (distance_to_goal / max_distance)

        # Apply collision penalty
        fitness -= self.collision_penalty

        # Bonus for getting very close to the goal
        if distance_to_goal < 2.0:  # within 1 unit of the goal
            fitness += 20  # reward for reaching the goal

        # Ensure fitness is non-negative
        fitness = max(0, fitness)


        filename = f"tmp{solutionID}.txt"
        file = open(filename, "w")
        # Write the final x-coordinate of link zero
        file.write(str(fitness))
        file.close()
        os.system(f"mv tmp{solutionID}.txt fitness{solutionID}.txt")

