import random

from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        # connecting to world
        self.physicsClient = p.connect(p.DIRECT)
        # p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # setting gravity
        p.setGravity(0, 0, -9.8)

        # creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        self.robotId = self.robot.robotId

        # additional setting up
        pyrosim.Prepare_To_Simulate(self.robotId)

        # **Add the goal block**
        goal_position = [0, 14, 0.5]  # Adjust this for your maze's exit

        goal_block = p.loadURDF("cube_small.urdf", goal_position, globalScaling=20)  # Scaling factor
        p.changeVisualShape(goal_block, -1, rgbaColor=[1, 0, 0, 1])  # Red block

    def Run(self):
        # running simulation at specified time lengths
        for t in range(c.vectorSize):
            p.stepSimulation()
            if self.directOrGUI == "GUI":
                time.sleep(c.simulationSpeed)
            # enabling sensing in the robot
            self.robot.Sense(t)
            # enabling "thinking" in the robot
            self.robot.Think()
            # enabling acting in the robot
            self.robot.Act(t, self.robotId)
    def __del__(self):
        # Save sensor values
        # for sensor in self.robot.sensors.values():
        #     sensor.Save_Values()
        #
        # # Save motor values
        # for motor in self.robot.motors.values():
        #     motor.Save_Values()

        p.disconnect()

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)