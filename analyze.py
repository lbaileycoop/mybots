import numpy as np
import matplotlib.pyplot as plt


# printing touch sensor values from array
backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

#print(backLegSensorValues)

plt.plot(backLegSensorValues)
plt.plot(frontLegSensorValues)
plt.show()