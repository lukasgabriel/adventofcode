# Advent of Code 2015, Day 8: Matchsticks. Part 2
# http://adventofcode.com/day/8#part2

string_chars = 0  # Initialize variable in global namespace


def main():
    solution = 0
    for line in open("./2015/8/2015_08.txt", "r", encoding="utf-8"):
        code_chars = len(line.strip())

        exec(
            f"string_chars=len({line.strip()})", globals()
        )  # Needless to say, don't use exec with untrusted inputs

        solution += code_chars - string_chars

    return f"The resulting number of characters is {solution}"


if __name__ == "__main__":
    print(main())
