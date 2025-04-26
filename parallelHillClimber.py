import csv
import os
import time

import numpy as np

from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self, world):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.world = world
        self.parents = {}
        self.nextAvailableID = 0
        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        # history: list of lists of fitnesses
        self.history = []

    # def Evolve(self):
    #     self.Evaluate(self.parents)
    #     for currentGeneration in range(c.numberOfGenerations):
    #         self.Evolve_For_One_Generation(currentGeneration + 1)

    def Evolve(self):
        # record initial population fitness
        self.Evaluate(self.parents)
        self._record_generation()

        for gen in range(1, c.numberOfGenerations+1):
            self.Spawn()
            self.Mutate()
            self.Evaluate(self.children)
            self.Select()
            self._record_generation()
            self.Print(gen)

        # after all generations, save to CSV
        self._save_history()

    def Evolve_For_One_Generation(self, generation):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print(generation)
        self.Select()

    def _record_generation(self):
        # capture each parent’s fitness in sorted key order
        fitnesses = [self.parents[k].fitness for k in sorted(self.parents)]
        self.history.append(fitnesses)

    def _save_history(self):
        filename = f"fitnessVals{self.world}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            # header: gen, p0, p1, …, pN-1, avg
            header = ["generation"] + [f"p{ i }" for i in range(c.populationSize)] + ["avg"]
            writer.writerow(header)
            for gen, fits in enumerate(self.history):
                avg = float(np.mean(fits))
                writer.writerow([gen] + fits + [avg])
        print(f"Saved fitness history for world {self.world!r} to {filename!r}")

    def Spawn(self):
        self.children = {}
        for parentID in self.parents:
            self.children[parentID] = copy.deepcopy(self.parents[parentID])
            self.children[parentID].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
    # def Evaluate(self, solutions):
    #     for parent in solutions:
    #         solutions[parent].Start_Simulation("DIRECT")
    #     for parent in solutions:
    #         solutions[parent].Wait_For_Simulation_To_End()

    def Evaluate(self, solutions):
        for sol in solutions.values():
            sol.Start_Simulation("DIRECT", self.world)
        for sol in solutions.values():
            sol.Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness > self.parents[key].fitness:
                self.parents[key] = copy.deepcopy(self.children[key])
    def Print(self, generation):
        print(f"\nGeneration {generation}:")
        for key in self.parents:
            parent_fitness = self.parents[key].fitness
            child_fitness = self.children[key].fitness
            print(f"Parent {key} fitness: {parent_fitness}   Child {key} fitness: {child_fitness}")
        print()

    def Show_First(self):
        print("Showing first robot (initial population)...")
        first_parent = self.parents[0]  # Pick the first parent
        first_parent.Start_Simulation("GUI", self.world)
        first_parent.Wait_For_Simulation_To_End()  # Ensure simulation completes
        print("First robot simulation complete.")
        time.sleep(1)  # Brief pause to avoid GUI conflicts

    # def Show_Best(self):
    #     best_parent = min(self.parents, key=lambda k: self.parents[k].fitness)
    #     self.parents[best_parent].Start_Simulation("GUI")

    def Show_Best(self):
        print("Showing best robot (after evolution)...")
        best_parent = max(self.parents, key=lambda k: self.parents[k].fitness)  # Use max for highest fitness
        self.parents[best_parent].Start_Simulation("GUI", self.world)
        self.parents[best_parent].Wait_For_Simulation_To_End()  # Ensure simulation completes
        print(f"\nMost fit robot after simulation is complete. Fitness: {self.parents[best_parent].fitness}\n")