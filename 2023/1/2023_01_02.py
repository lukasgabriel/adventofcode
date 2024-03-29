# Advent of Code 2015, Day 1: Trebuchet?! Part 2
# https://adventofcode.com/2013/day/1#part2


import re


DIGITS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def main():
    solution = 0

    for line in open("./2023/1/2023_01.txt", "r", encoding="utf-8"):
        digits = re.findall(r"\d", line)

        print(line)
        for n, digit in enumerate(DIGITS):
            print(re.findall(DIGITS[n], line))

        solution += int("".join(digits[0] + digits[-1]))
       
    return f"The sum of all values is {solution}"


if __name__ == "__main__":
    print(main())
