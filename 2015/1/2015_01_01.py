# Advent of Code 2015, Day 1: Not Quite Lisp. Part 1
# http://adventofcode.com/day/1


def main():
    puzzle_input = open("./input.txt", "r").readlines()[0]
    puzzle_solution = puzzle_input.count("(") - puzzle_input.count(")")
    return (
        f"Santa will end up on floor {puzzle_solution}"
    )


if __name__ == "__main__":
    print(main())
