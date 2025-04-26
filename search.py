import sys
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# creating instance of hillclimber
# phc = PARALLEL_HILL_CLIMBER()
# phc.Evolve()
world = sys.argv[1]         # expect "A" or "B"
phc = PARALLEL_HILL_CLIMBER(world)
phc.Evolve()

phc.Show_First()
phc.Show_Best()
