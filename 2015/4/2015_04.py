# Advent of Code 2015, Day 4: The Ideal Stocking Stuffer. Part 1 & 2
# http://adventofcode.com/day/4

from hashlib import md5


PUZZLE_INPUT = "ckczppom"


def main():
    suffix = 0
    hashval = 0x00
    solution_5_zeroes = None

    while True:
        suffix += 1
        hashval = md5(str(PUZZLE_INPUT + str(suffix)).encode("utf-8")).hexdigest()

        if str(hashval)[0:5] == "00000" and solution_5_zeroes is None:
            solution_5_zeroes = suffix
            continue

        if str(hashval)[0:6] == "000000":
            solution_6_zeroes = suffix
            return f"The required suffix for five zeroes is {solution_5_zeroes}, the suffix for six zeroes is {solution_6_zeroes}"


if __name__ == "__main__":
    print(main())
