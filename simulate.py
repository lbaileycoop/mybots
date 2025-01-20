import pybullet as p
import time
import pybullet_data

# connecting to world
physicsClient = p.connect(p.GUI)
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.setAdditionalSearchPath(pybullet_data.getDataPath())


# setting gravity
p.setGravity(0,0,-9.8)

# setting the floor
planeId = p.loadURDF("plane.urdf")

# loading in box
p.loadSDF("box.sdf")

# running simulation at specified time lengths
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()
