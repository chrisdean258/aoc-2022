#!/usr/bin/env python3

class Monkey:
    monkeys = []

    def __init__(self, starting, op, op_val, test, true, false):
        self.items = starting
        self.op = op
        self.op_val = op_val
        self.test = test
        self.true = true
        self.false = false
        self.tot = 0

    def throw_items(self):
        self.tot += len(self.items)
        for item in self.items:
            if self.op == "square":
                item = item * item
            elif self.op == "add":
                item = item + self.op_val
            elif self.op == "mul":
                item = item * self.op_val
            else:
                assert False, self.op
            item //= 3
            if item % self.test == 0:
                Monkey.monkeys[self.true].append(item)
            else:
                Monkey.monkeys[self.false].append(item)
        self.items = []

    def append(self, item):
        self.items.append(item)


starting, op, test, true, false, op_val = [None] * 6
for line in open(0):
    if line.startswith("Monkey"):
        if starting:
            Monkey.monkeys.append(
                Monkey(starting, op, op_val, test, true, false))
    elif "Starting" in line:
        starting = [int(i) for i in line.partition(":")[2].strip().split(", ")]
    elif "Operation" in line:
        if "old * old" in line:
            op_val = None
            op = "square"
        elif "+" in line:
            op_val = int(line.split()[-1])
            op = "add"
        else:
            op_val = int(line.split()[-1])
            op = "mul"
    elif "true" in line:
        true = int(line.strip().split()[-1])
    elif "false" in line:
        false = int(line.strip().split()[-1])
    elif "Test" in line:
        test = int(line.split()[-1])
Monkey.monkeys.append(Monkey(starting, op, op_val, test, true, false))

for i in range(20):
    for monkey in Monkey.monkeys:
        monkey.throw_items()

a, b = sorted([m.tot for m in Monkey.monkeys])[-2:]
print(a * b)
