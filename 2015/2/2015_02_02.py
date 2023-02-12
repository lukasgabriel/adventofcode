# Advent of Code 2015, Day 2: I Was Told There Would Be No Math. Part 2
# http://adventofcode.com/day/2#part2


def main():
    total_length = 0

    for line in open("./2015/2/2015_02.txt", "r", encoding="utf-8"):
        sides = sorted([int(i) for i in line.split("x")])
        ribbon = 2 * sides[0] + 2 * sides[1]
        bow = sides[0] * sides[1] * sides[2]
        total_length += ribbon + bow

    return f"The elves will need {total_length} feet of ribbon."


if __name__ == "__main__":
    print(main())
