import numpy as np
import matplotlib.pyplot as plt


# printing touch sensor values from array
sensorValues = np.load('data/sensorValues.npy')
motorValues = np.load('data/motorValues.npy')

# Plotting Sensor Values
plt.plot(sensorValues, label='sensorValues', linewidth=2)
plt.title('Sensor Commands')
plt.legend()
plt.show()

# Plotting Motor Values
plt.plot(motorValues, label='motorValues', linewidth=2)
plt.title('Motor Commands')
plt.legend()
plt.show()

