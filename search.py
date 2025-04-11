import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# creating instance of hillclimber
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_First()
phc.Show_Best()
