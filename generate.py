import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

length = 10
width = 1
height = 1

pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.Send_Cube(name="Box2", pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.Send_Cube(name="Box3", pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.End()


