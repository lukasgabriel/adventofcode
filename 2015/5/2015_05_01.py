# Advent of Code 2015, Day 5: Doesn't He Have Intern-Elves For This? Part 1
# http://adventofcode.com/day/5

from re import findall

def main():
    nice_strings_count = 0

    for line in open("./2015/5/2015_05.txt", "r", encoding="utf-8"):
        vowel_count = len(findall(r"[aeiou]", line))
        letter_twice_count = len(findall(r"(.)\1+", line))
        forbidden_strings_count = len(findall(r"ab|cd|pq|xy", line))
        
        if vowel_count >= 3 and letter_twice_count >= 1 and forbidden_strings_count == 0:
            nice_strings_count += 1
    
    return f"There are {nice_strings_count} nice strings in the list."


if __name__ == "__main__":
    print(main())
