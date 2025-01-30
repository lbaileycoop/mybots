import math
import numpy as np
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.vectorSize)
        self.Prepare_To_Act()
    def Prepare_To_Act(self):
        self.amplitude = c.Amplitude
        self.frequency = c.Frequency
        self.offset = c.PhaseOffset

        # modifying the specified motor's frequency by half
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.Frequency / 2

            # compute the target angle using amplitude, frequency, and phase offset
        for t in range(c.vectorSize):
            self.motorValues[t] = self.amplitude * math.sin(self.frequency * t + self.offset)
    def Set_Value(self, t, robotId):
        # simulating a motor that supplies force to one of the robot's joints
        # bodyIndex tells the simulator that we are about to simulate a motor in the robot called robotId
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL,
                                    targetPosition=self.motorValues[t], maxForce=50)
    def Save_Values(self):
        np.save('data/motorValues.npy', self.motorValues)
