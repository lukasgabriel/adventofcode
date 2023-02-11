# Advent of Code 2015, Day 3: Perfectly Spherical Houses in a Vacuum. Part 1
# http://adventofcode.com/day/3


def main():
    houses = 0
    coordinates = []
    location = [0, 0]

    for line in open("./2015/3/2015_03.txt", "r", encoding="utf-8"):
        for instruction in line:
            coordinates.append(str(location))
            location[0] = location[0] + 1 if instruction == ">" else location[0]
            location[0] = location[0] - 1 if instruction == "<" else location[0]
            location[1] = location[1] + 1 if instruction == "^" else location[1]
            location[1] = location[1] - 1 if instruction == "v" else location[1]
    coordinates.append(str(location))
    houses = len(set(coordinates))

    return f"Santa will visit {houses} unique houses."


if __name__ == "__main__":
    print(main())
