# Advent of Code 2015, Day 3: Perfectly Spherical Houses in a Vacuum. Part 2
# http://adventofcode.com/day/3


def main():
    houses = 0
    coordinates = []
    counter = 0
    location_s = [0, 0]
    location_r = [0, 0]

    for line in open("./2015/3/2015_03.txt", "r", encoding="utf-8"):
        for instruction in line:
            if counter % 2 == 0:
                coordinates.append(str(location_s))
                location_s[0] = (
                    location_s[0] + 1 if instruction == ">" else location_s[0]
                )
                location_s[0] = (
                    location_s[0] - 1 if instruction == "<" else location_s[0]
                )
                location_s[1] = (
                    location_s[1] + 1 if instruction == "^" else location_s[1]
                )
                location_s[1] = (
                    location_s[1] - 1 if instruction == "v" else location_s[1]
                )
            else:
                coordinates.append(str(location_r))
                location_r[0] = (
                    location_r[0] + 1 if instruction == ">" else location_r[0]
                )
                location_r[0] = (
                    location_r[0] - 1 if instruction == "<" else location_r[0]
                )
                location_r[1] = (
                    location_r[1] + 1 if instruction == "^" else location_r[1]
                )
                location_r[1] = (
                    location_r[1] - 1 if instruction == "v" else location_r[1]
                )
            counter += 1
    coordinates.append(str(location_r))
    coordinates.append(str(location_s))
    houses = len(set(coordinates))

    return f"Santa and Robo-Santa will visit {houses} unique houses."


if __name__ == "__main__":
    print(main())
