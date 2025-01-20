import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

<<<<<<< HEAD
length = 10
width = 1
height = 1

pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.Send_Cube(name="Box2", pos=[0, 0, 0.5], size=[length, width, height])

pyrosim.Send_Cube(name="Box3", pos=[0, 0, 0.5], size=[length, width, height])
=======
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
>>>>>>> 3dd1af760258c8481ee8041b554f5cf9bb4b54ac

pyrosim.End()


