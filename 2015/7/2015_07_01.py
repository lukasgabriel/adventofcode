# Advent of Code 2015, Day 7: Some Assembly Required. Part 1
# http://adventofcode.com/day/7

from re import findall
from uuid import uuid4


class Wire:
    def __init__(self, id: str):
        self.id = id
        self.signal = 0
        self.connection_in = None
        self.connections_out = []

    def __str__(self):
        return f"[{self.connection_in}] --> ({self.id}) --> {self.connections_out}"

    def connect_in(self, source: "Wire" or "Gate"):
        if self.connection_in:
            raise Exception
        self.connection_in = source

    def connect_out(self, target: "Wire" or "Gate"):
        target.connect_in(self)
        self.connections_out.append(target)

    def send(self, signal):
        self.signal = signal
        for connection in self.connections_out:
            connection.send(signal)


class Gate:
    def __init__(self, operation: str, shift: int|None):
        self.id = str(uuid4())[:4]
        self.operation = operation
        self.signal = 0
        self.shift = shift if shift else None
        self.connections_in = []
        self.connections_out = []

        assert operation in ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]
        if operation in ["LSHIFT", "RSHIFT"]:
            assert shift

    def __str__(self):
        return f"[{self.connections_in}] --> ({self.id}: {self.operation}) --> {self.connections_out}"

    def connect_in(self, source: "Wire" or "Gate"):
        if len(self.connections_in) > 2:
            raise Exception
        self.connections_in.append(source)

    def connect_out(self, target: "Wire" or "Gate"):
        target.connect_in(self)
        self.connections_out.append(target)

    def apply_operation(self):
        if self.operation == "AND":
            self.signal = self.connections_in[0] & self.connections_in[1]
        if self.operation == "OR":
            self.signal = self.connections_in[0] | self.connections_in[1]
        if self.operation == "NOT":
            self.signal = ~self.connections_in[0]
        if self.operation == "LSHIFT":
            self.signal = self.connections_in[0] << self.shift
        if self.operation == "RSHIFT":
            self.signal = self.connections_in[0] >> self.shift

    def send(self, signal):
        self.apply_operation()
        for connection in self.connections_out:
            connection.send(signal) 


def main():
    circuit = {}
    
    for line in open("./2015/6/2015_07.txt", "r", encoding="utf-8"):
        operation = findall(r"(AND|OR|NOT|LSHIFT|RSHIFT)", line)[0]
        if operation:
            left, right = line.split("->")
            if operation == "AND":
                gate = Gate(operation, shift=None)
                inputs = left.split(operation)
                for input in inputs:
                    if float()
                circuit[gate.id] = gate


    return


if __name__ == "__main__":
    print(main())
