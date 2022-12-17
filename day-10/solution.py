def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        cycles = 0
        temp = 0
        x = 1
        printed = False
        out = 0
        for line in lines:
            if ((cycles - 20) % 40 == 0 or (cycles - 20) % 40 == 1) and not printed:
                print(f"{round(cycles, -1)}: {round(cycles,-1) * x}")
                out += round(cycles, -1) * x
                printed = True
            else:
                printed = False
            x += temp
            if "addx" in line:
                cycles += 2
                temp = int(line.split()[1])
                # print(f"cycles: {cycles}", x)
            else:
                cycles += 1
                temp = 0

    return out


def printCRT(cycles, x):

    if cycles == x or cycles + 1 == x or cycles - 1 == x:
        print("#", end="")
    else:
        print(".", end="")

    if cycles == 39:
        print("")
        return -1
    return cycles


def main2():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        cycles = 0
        x = 1
        out = 0
        new_val = 0
        for line in lines:
            if "add" in line:
                new_val = int(line.split()[1])
                cycles = printCRT(cycles, x)
                cycles += 1
                cycles = printCRT(cycles, x)
                cycles += 1
            else:
                new_val = 0
                cycles = printCRT(cycles, x)
                cycles += 1
            x += new_val

    print("\n")

    # return out


if __name__ == "__main__":

    print(main())
    main2()
