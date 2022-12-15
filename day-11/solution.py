class Monkey:
    def __init__(self, num, items, op, test, t, f) -> None:
        self.num = num
        self.items = items
        self.test = test
        self.op = op
        self.t = t
        self.f = f
        self.inspections = 0

    def operate(self, old):
        old = old
        return eval(self.op)


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        monkeys = []
        for i in range(0, len(lines), 7):
            num = int(lines[i].split()[1][0])
            items = lines[i + 1].split(": ")[1].split(", ")
            items = [int(i) for i in items]
            test = int(lines[i + 3].split(" ")[-1])
            t = int(lines[i + 4].split(" ")[-1])
            f = int(lines[i + 5].split(" ")[-1])
            op = lines[i + 2].split("= ")[1]
            # print(op)
            m = Monkey(num, items, op, test, t, f)
            monkeys.append(m)

    for rounds in range(20):
        for i, monkey in enumerate(monkeys):
            # print("monkey number: ", i)
            while monkey.items:
                w = monkey.items.pop(0)
                monkey.inspections += 1
                w = monkey.operate(w)
                w = w // 3
                # print(w)
                if w % monkey.test == 0:
                    monkeys[monkey.t].items.append(w)
                else:
                    monkeys[monkey.f].items.append(w)

        # print("after round:")
        # for i in monkeys:
        #     print(f"monkey {i.num}: {i.items}")
    for i in monkeys:
        print(f"monkey {i.num}: {i.inspections}")

    ls = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
    return ls[0].inspections * ls[1].inspections


def main2():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        monkeys = []
        for i in range(0, len(lines), 7):
            num = int(lines[i].split()[1][0])
            items = lines[i + 1].split(": ")[1].split(", ")
            items = [int(i) for i in items]
            test = int(lines[i + 3].split(" ")[-1])
            t = int(lines[i + 4].split(" ")[-1])
            f = int(lines[i + 5].split(" ")[-1])
            op = lines[i + 2].split("= ")[1]
            m = Monkey(num, items, op, test, t, f)
            monkeys.append(m)

    for rounds in range(1000):
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                w = monkey.items.pop(0)
                monkey.inspections += 1
                w = monkey.operate(w)
                if w % monkey.test == 0:
                    monkeys[monkey.t].items.append(w)
                else:
                    monkeys[monkey.f].items.append(w)

    for i in monkeys:
        print(f"monkey {i.num}: {i.inspections}")

    # ls = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
    # return ls[0].inspections * ls[1].inspections


if __name__ == "__main__":
    print(main())
    print(main2())
