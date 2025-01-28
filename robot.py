import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")

        self.sensors = {}
        self.motors = {}