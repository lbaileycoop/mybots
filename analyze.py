import numpy as np
import matplotlib.pyplot as plt


# printing touch sensor values from array
backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
backLegTargetAngles = np.load('data/backLegTargetAngles.npy')
frontLegTargetAngles = np.load('data/frontLegTargetAngles.npy')


#print(backLegSensorValues)

# plt.plot(backLegSensorValues, label='backLegSensorValues', linewidth=5)
# plt.plot(frontLegSensorValues, label='frontLegSensorValues', linewidth=2)
plt.plot(backLegTargetAngles, label='backLegTargetAngles', linewidth=5)
plt.plot(frontLegTargetAngles, label='frontLegTargetAngles', linewidth=2)
plt.title('Motor Commands')
plt.legend()
plt.show()