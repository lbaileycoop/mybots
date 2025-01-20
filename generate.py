import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# assigning box variables
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

# defining grid values
rows = 5
columns = 5

for x in range(rows):
    for y in range(columns):
        # resetting variables for tower dimensions
        z = 0.5
        current_length = length
        current_width = width
        current_height = height
        # creating multiple boxes
        for i in range(10):
            # creating boxes
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[current_length, current_width, current_height])
            # making each box stack on top of each other
            z += height
            # making each box 90% of the size of the box before it
            current_length *= 0.9
            current_width *= 0.9
            current_height *= 0.9

pyrosim.End()


