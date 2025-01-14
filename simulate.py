import pybullet as p

physicsClient = p.connect(p.GUI)

for (int i = 0; i < 1000; i++) {
    p.stepSimulation();
}


p.disconnect()
