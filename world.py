import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class WORLD:

    def __init__(self):
        # setting the floor
        self.planeId = p.loadURDF("plane.urdf")

        # loading in box
        p.loadSDF("world.sdf")