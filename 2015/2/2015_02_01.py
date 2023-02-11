# Advent of Code 2015, Day 2: I Was Told There Would Be No Math. Part 1
# http://adventofcode.com/day/2


def main():
    total_area = 0

    for line in open("./2015/2/2015_02.txt", "r", encoding="utf-8"):
        l, w, h = [int(i) for i in line.split("x")]
        sides = 2*l*w, 2*w*h, 2*h*l
        total_area += sum(sides) + min(sides) / 2

    return f"The elves will need {total_area} square feet of wrapping paper."


if __name__ == "__main__":
    print(main())
