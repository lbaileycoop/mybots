import numpy as np
import matplotlib.pyplot as plt


# printing touch sensor values from array
backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

#print(backLegSensorValues)

plt.plot(backLegSensorValues, label='backLegSensorValues', linewidth=5)
plt.plot(frontLegSensorValues, label='frontLegSensorValues', linewidth=2)
plt.legend()
plt.show()