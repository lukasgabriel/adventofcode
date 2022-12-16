# Advent of Code 2015, Day 1: Not Quite Lisp. Part 1
# http://adventofcode.com/day/1


def main():
    puzzle_input = input("Please enter the puzzle input: ")
    puzzle_solution = puzzle_input.count("(") - puzzle_input.count(")")
    return (
        f"Given the input {puzzle_input}, Santa will end up on floor {puzzle_solution}"
    )


if __name__ == "__main__":
    print(main())
