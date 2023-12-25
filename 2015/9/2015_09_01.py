# Advent of Code 2015, Day 9: All in a Single Night. Part 1
# https://adventofcode.com/2015/day/9

import re
import networkx as nx


def main():
    solution = 0
    pairings = []

    # Get pairings and distances from file
    for line in open("./2015/9/2015_09.txt", "r", encoding="utf-8"):
        pairings.append(re.split(r" to | = ", line.strip()))

    # Build graph
    G = nx.Graph()
    for pairing in pairings:
        G.add_edge(pairing[0], pairing[1], weight=int(pairing[2]))

    # Find shortest path visiting every node exactly once by brute force
    
       
    return f"The shortest possible distance is {solution}"


if __name__ == "__main__":
    print(main())
