# Advent of Code 2015, Day 10: Elves Look, Elves Say. Part 2
# https://adventofcode.com/2015/day/10#part2


def main():
    ITERATIONS = 50

    input = open("./2015/10/2015_10.txt", "r", encoding="utf-8").readline().strip()
    
    output = ""
    counter = 1
    for _ in range(ITERATIONS):
        output = ""
        for i in range(len(input)):
            if i < len(input) - 1 and input[i] == input[i + 1]:
                counter += 1
            else:
                output += str(counter) + input[i]
                counter = 1
        input = output


    return f"The length of the ouput is {len(output)}."


if __name__ == "__main__":
    print(main())
