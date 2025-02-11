from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]

# connecting to simulation class
simulation = SIMULATION(directOrGUI)

# Call the Run method to start the simulation
simulation.Run()
simulation.Get_Fitness()
