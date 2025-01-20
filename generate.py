import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# assigning box variables
length = 1
width = 1
height = 1

x = 0
y = 0
z = 0.5
for i in range(10):
    # creating boxes
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    # making each box stack on top of each other
    z = z + 1
    # making each box 90% of the size of the box before it
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9

pyrosim.End()


