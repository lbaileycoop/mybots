import os
from hillclimber import HILL_CLIMBER

for i in range(2):
    # os.system("python3 generate.py")
    # os.system("python3 simulate.py")
    os.system("python3 hillclimber.py")

    # creating instance of hillclimber
    hc = HILL_CLIMBER()
    hc.Evolve()
    hc.Show_Best()
