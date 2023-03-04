# Advent of Code 2015, Day 7: Some Assembly Required. Part 2
# http://adventofcode.com/day/7#part2

from re import findall, match
from uuid import uuid4
from sys import argv


class Wire:
    def __init__(self, id: str):
        self.id = id
        self.signal = None
        self.connection_in = None
        self.connections_out = []
        self.visited = 0

    def __repr__(self):
        c_in = (
            self.connection_in.id
            if type(self.connection_in) in [Wire, Gate]
            else self.connection_in
        )
        sig = (
            self.connection_in.signal
            if type(self.connection_in) in [Wire, Gate]
            else self.connection_in
        )
        return f"[{c_in}] with {sig} --> ({self.id}: {self.signal}) --> {[conn.id for conn in self.connections_out] if len(self.connections_out) else [None]} with {self.signal}"

    def connect_in(self, source: "Wire" or "Gate" or int):
        if self.connection_in:
            raise Exception
        if type(source) == int:
            self.signal = source
        self.connection_in = source

    def connect_out(self, target: "Wire" or "Gate"):
        target.connect_in(self)
        self.connections_out.append(target)

    def send(self, signal):
        if self.visited >= 2:
            print(
                f"[Wire {self.id} with signal {self.signal}] visited too many times. Skipping..."
            )
            return
        
        if self.id == "b":
            signal = argv[2]

        self.signal = signal
        for connection in self.connections_out:
            print(f"Sending {self.signal} to {connection.id}")
            connection.send(self.signal)


class Gate:
    MASK = (1 << 16) - 1  # creates a 16-bit mask of all 1's

    def __init__(self, operation: str, shift: int | None):
        self.id = str(uuid4())[:6]
        self.operation = operation
        self.signal = None
        self.shift = shift if shift else None
        self.connections_in = []
        self.connection_out = None
        self.visited = 0

        assert operation in ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]
        if operation in ["LSHIFT", "RSHIFT"]:
            assert shift

    def __repr__(self):
        c_in = []
        sig = []
        for conn in self.connections_in:
            if type(conn) == int:
                c_in.append(conn)
                sig.append(conn)
            elif type(conn) == Wire:
                c_in.append(conn.id)
                sig.append(conn.signal)
            elif not conn:
                c_in.append(None)
                sig.append(None)
        return f"{c_in} with {sig} --> ({self.id}: {self.operation}{(' ' + self.shift if self.shift else '')}) --> {self.connection_out.id} with {self.signal}"

    def connect_in(self, source: "Wire" or "Gate" or int):
        if len(self.connections_in) > 2:
            raise Exception
        self.connections_in.append(source)

    def connect_out(self, target: "Wire" or "Gate"):
        target.connect_in(self)
        self.connection_out = target

    def apply_operation(self):
        c_in = []
        sig = []
        for conn in self.connections_in:
            if type(conn) == int:
                c_in.append(conn)
                sig.append(conn)
            elif type(conn) == Wire:
                c_in.append(conn.id)
                sig.append(conn.signal)
            elif not conn:
                c_in.append(None)
                sig.append(None)
        print(f"Applying {self.operation} to {c_in} with signals {sig}")

        if self.operation == "AND":
            self.signal = int(
                self.connections_in[0].signal
                if type(self.connections_in[0]) == Wire
                else self.connections_in[0]
            ) & int(
                self.connections_in[1].signal
                if type(self.connections_in[1]) == Wire
                else self.connections_in[1]
            )
        if self.operation == "OR":
            self.signal = int(self.connections_in[0].signal) | int(
                self.connections_in[1].signal & Gate.MASK
            )
        if self.operation == "NOT":
            self.signal = ~int(self.connections_in[0].signal) & Gate.MASK
        if self.operation == "LSHIFT":
            self.signal = (
                int(self.connections_in[0].signal) << int(self.shift) & Gate.MASK
            )
        if self.operation == "RSHIFT":
            self.signal = (
                int(self.connections_in[0].signal) >> int(self.shift) & Gate.MASK
            )

    def send(self, signal):
        if self.visited >= 2:
            print(
                f"[{self.operation} Gate {self.id}] visited too many times. Skipping..."
            )
            return
        self.visited += 1
        for connection in self.connections_in:
            if not type(connection) == int:
                if connection.signal == None:
                    print(
                        f"[{self.operation} Gate {self.id}] One or more connections have no signal. Skipping..."
                    )
                    return

        self.apply_operation()
        print(f"Sending {self.signal} to {self.connection_out.id}")
        self.connection_out.send(self.signal)


def main():
    circuit = {}

    for line in open("./2015/7/2015_07.txt", "r", encoding="utf-8"):
        try:
            operation = findall(r"(AND|OR|NOT|LSHIFT|RSHIFT)", line)[0]
        except:
            operation = None

        if operation:
            left, right = line.split("->")
            left = left.strip()
            right = right.strip()

            if operation in ["AND", "OR"]:
                gate = Gate(operation, shift=None)
                inputs = left.split(operation)

                for input in inputs:
                    input = input.strip()

                    if input.isdecimal():
                        gate.connect_in(source=int(input))
                    else:
                        if not input in circuit:
                            wire_left = Wire(id=input)
                            circuit[wire_left.id] = wire_left
                        circuit[input].connect_out(gate)

            if operation == "NOT":
                gate = Gate(operation, shift=None)
                input = left.split(operation)[1].strip()

                if not input in circuit:
                    wire_left = Wire(id=input)
                    circuit[wire_left.id] = wire_left
                circuit[input].connect_out(gate)

            if operation in ["LSHIFT", "RSHIFT"]:
                inputs = left.split(operation)
                inputs = [input.strip() for input in inputs]
                gate = Gate(operation, shift=inputs[1])

                if not inputs[0] in circuit:
                    wire_left = Wire(id=inputs[0])
                    circuit[wire_left.id] = wire_left
                circuit[inputs[0]].connect_out(gate)

            if not right in circuit:
                wire_right = Wire(id=right)
                circuit[wire_right.id] = wire_right
            gate.connect_out(circuit[right])
            circuit[gate.id] = gate

        elif match(r"^\d+ -> [A-Za-z]+$", line):
            left, right = line.split("->")
            left = left.strip()
            right = right.strip()

            if not right in circuit:
                wire_right = Wire(id=right)
                circuit[wire_right.id] = wire_right

            circuit[right].connect_in(int(left))

        elif match(r"^[A-Za-z]+ -> [A-Za-z]+$", line):
            left, right = line.split("->")
            left = left.strip()
            right = right.strip()

            if not left in circuit:
                wire_left = Wire(id=left)
                circuit[wire_left.id] = wire_left

            if not right in circuit:
                wire_right = Wire(id=right)
                circuit[wire_right.id] = wire_right

            circuit[left].connect_out(circuit[right])


    print("\n---\tCircuit Simulation 1:\t---\n")
    for item in circuit.items():
        print(f"{item[0]}:\t{item[1]}")
        if type(item[1]) == Wire and type(item[1].connection_in) == int:
            item[1].send(item[1].connection_in)

    print("\n---\tFinal Values 1:\t---\n")
    for item in circuit.items():
        if type(item[1]) == Wire:
            print(f"{item[1].id}: {item[1].signal}")

    return f"\n---\tFinal value of wire {argv[1]}: {circuit[argv[1]].signal}\t---\n"


if __name__ == "__main__":
    print(main())
