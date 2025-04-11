import os
import time

from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration + 1)

    def Evolve_For_One_Generation(self, generation):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print(generation)
        self.Select()

    def Spawn(self):
        self.children = {}
        for parentID in self.parents:
            self.children[parentID] = copy.deepcopy(self.parents[parentID])
            self.children[parentID].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
    def Evaluate(self, solutions):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT")
        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()
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
        first_parent.Start_Simulation("GUI")
        first_parent.Wait_For_Simulation_To_End()  # Ensure simulation completes
        print("First robot simulation complete.")
        time.sleep(1)  # Brief pause to avoid GUI conflicts

    # def Show_Best(self):
    #     best_parent = min(self.parents, key=lambda k: self.parents[k].fitness)
    #     self.parents[best_parent].Start_Simulation("GUI")

    def Show_Best(self):
        print("Showing best robot (after evolution)...")
        best_parent = max(self.parents, key=lambda k: self.parents[k].fitness)  # Use max for highest fitness
        self.parents[best_parent].Start_Simulation("GUI")
        self.parents[best_parent].Wait_For_Simulation_To_End()  # Ensure simulation completes
        print(f"Best robot (ID {best_parent}) simulation complete. Fitness: {self.parents[best_parent].fitness}")