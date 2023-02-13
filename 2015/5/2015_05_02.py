# Advent of Code 2015, Day 5: Doesn't He Have Intern-Elves For This? Part 2
# https://adventofcode.com/2015/day/5#part2

from re import findall

def main():
    nice_strings_count = 0

    for line in open("./2015/5/2015_05.txt", "r", encoding="utf-8"):
        unique_pairs_count = len(findall(r"(..).*\1", line))
        repeat_with_gap_count = len(findall(r"([a-z])[a-z]\1", line))
        
        if unique_pairs_count >= 1 and repeat_with_gap_count >= 1:
            nice_strings_count += 1
    
    return f"There are {nice_strings_count} nice strings in the list."


if __name__ == "__main__":
    print(main())
