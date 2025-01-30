import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.vectorSize)
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # # prints sensor values
        # if t == c.vectorSize - 1:
        #     print(self.values)
    def Save_Values(self):
        np.save('data/SensorValues.npy', self.values)
