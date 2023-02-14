# Advent of Code 2015, Day 7: Some Assembly Required. Part 1
# http://adventofcode.com/day/7

from re import findall


class Wire:
    def __init__(self, id):
        self.id = id
        self.signal = 0
        self.connection = None

    def connect(self, target):
        target.connect(self)
        self.connection = target

    


def main():
    
    for line in open("./2015/6/2015_06.txt", "r", encoding="utf-8"):
        instruction = findall(r"(turn on|turn off|toggle)", line)[0]

    return


if __name__ == "__main__":
    print(main())
