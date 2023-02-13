# Advent of Code 2015, Day 6: Probably a Fire Hazard. Part 1
# http://adventofcode.com/day/6

from re import findall

def main():
    lights = [[0 for _ in range(0, 9)] for _ in range(0, 9)]
    
    for line in open("./2015/6/2015_06.txt", "r", encoding="utf-8"):
        instruction = findall(r"(turn on|turn off|toggle)", line)[0]
        a, b, *_ = findall(r"\d{1,3},\d{1,3}", line)

        if instruction == "turn on":
            lights

    return(sum([sum(row) for row in lights]))


if __name__ == "__main__":
    print(main())
