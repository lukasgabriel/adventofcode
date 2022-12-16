# Advent of Code 2015, Day 1: Not Quite Lisp. Part 2
# http://adventofcode.com/day/1#part2


def main():
    puzzle_input = input("Please enter the puzzle input: ")

    position, current_floor = 0, 0
    while current_floor >= 0:
        current_floor = (
            current_floor + 1 if puzzle_input[position] == "(" else current_floor - 1
        )
        position += 1

    return f"Given the input {puzzle_input}, Santa will enter the basement at position {position}"


if __name__ == "__main__":
    print(main())
