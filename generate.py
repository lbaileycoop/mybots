import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    # assigning box variables
    length = 1
    width = 1
    height = 1
    x = -2
    y = 2
    z = 0.5

    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    # defining grid values
    # rows = 5
    # columns = 5

    # for x in range(rows):
    #     for y in range(columns):
    #         # resetting variables for tower dimensions
    #         z = 0.5
    #         current_length = length
    #         current_width = width
    #         current_height = height
    #         # creating multiple boxes
    #         for i in range(10):
    #             # creating boxes
    #             pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[current_length, current_width, current_height])
    #             # making each box stack on top of each other
    #             z += height
    #             # making each box 90% of the size of the box before it
    #             current_length *= 0.9
    #             current_width *= 0.9
    #             current_height *= 0.9

    # ending program
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # assigning torso variables
    length = 1
    width = 1
    height = 1
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1])
    pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])
    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[length, width, height])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0, 1, 0])
    pyrosim.Send_Cube(name="Link4", pos=[0, 0.5, 0], size=[length, width, height])
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0, 1, -1])
    pyrosim.Send_Cube(name="Link5", pos=[0, -0.5, 0], size=[length, width, height])
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0, 0, -1])
    pyrosim.Send_Cube(name="Link6", pos=[0, -0.5, 0], size=[length, width, height])


    # ending program
    pyrosim.End()

Create_World()
Create_Robot()

