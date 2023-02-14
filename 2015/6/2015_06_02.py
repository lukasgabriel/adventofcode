# Advent of Code 2015, Day 6: Probably a Fire Hazard. Part 2
# http://adventofcode.com/day/6#part2

from re import findall
import numpy as np

def main():
    #lights = [[0 for _ in range(0, 9)] for _ in range(0, 9)]
    lights = np.zeros((1000, 1000), dtype=np.int8)
    
    for line in open("./2015/6/2015_06.txt", "r", encoding="utf-8"):
        instruction = findall(r"(turn on|turn off|toggle)", line)[0]
        a, b, *_ = findall(r"\d{1,3},\d{1,3}", line)
        a1, a2 = [int(x) for x in a.split(",")]
        b1, b2 = [int(x) for x in b.split(",")]
        
        if instruction == "turn on":
            lights[a1:b1+1, a2:b2+1] += 1
        if instruction == "turn off":
            lights[a1:b1+1, a2:b2+1] -= 1
        if instruction == "toggle":
            lights[a1:b1+1, a2:b2+1] += 2

        lights = np.clip(lights, 0, 255)
    
    return(np.sum(lights))


if __name__ == "__main__":
    print(main())
