"""
plot_history.py

Usage:
    python plot_history.py fitness_history_A.csv fitness_history_B.csv

This script reads the average fitness per generation from two CSV files
and plots both curves on the same graph for comparison.
"""
import sys
import csv
import matplotlib.pyplot as plt


def load_history(filename):
    """Load generation numbers and average fitness from a CSV file."""
    generations = []
    averages = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            generations.append(int(row['generation']))
            averages.append(float(row['avg']))
    return generations, averages


def main():
    if len(sys.argv) != 3:
        print("Usage: python plot_history.py fitness_history_A.csv fitness_history_B.csv")
        sys.exit(1)

    fileA, fileB = sys.argv[1], sys.argv[2]
    gensA, avgA = load_history(fileA)
    gensB, avgB = load_history(fileB)

    plt.plot(gensA, avgA, label='World A')
    plt.plot(gensB, avgB, label='World B')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.xticks()
    plt.yticks()
    plt.title('Evolution of Average Fitness: World A vs. World B')
    plt.legend()
    plt.tight_layout()
    plt.savefig("FitnessPlot.png", dpi=300, bbox_inches="tight")
    print("Saved plot")


if __name__ == '__main__':
    main()
