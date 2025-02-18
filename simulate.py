from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

# connecting to simulation class
simulation = SIMULATION(directOrGUI, solutionID)

# Call the Run method to start the simulation
simulation.Run()
simulation.Get_Fitness(solutionID)
