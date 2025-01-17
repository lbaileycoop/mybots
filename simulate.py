import pybullet as p
import time

# connecting to world
physicsClient = p.connect(p.GUI)
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# settign gravity
p.setGravity(0,0,-9.8)

# loading in box
p.loadSDF("box.sdf")

# running simulation at specified time lengths
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
	
# disconnecting from world
p.disconnect()
