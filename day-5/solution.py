# [T]             [P]     [J]        
# [F]     [S]     [T]     [R]     [B]
# [V]     [M] [H] [S]     [F]     [R]
# [Z]     [P] [Q] [B]     [S] [W] [P]
# [C]     [Q] [R] [D] [Z] [N] [H] [Q]
# [W] [B] [T] [F] [L] [T] [M] [F] [T]
# [S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
# [Q] [Q] [B] [D] [J] [W] [H] [R] [J]
#  1   2   3   4   5   6   7   8   9

stacks1 = {
    1: list("ZN"),
    2: list("MCD"),
    3: list("P"),
}

stacks2 = {
    1: list("QSWCZVFT"),
    2: list("QRB"),
    3: list("BZTQPMS"),
    4: list("DVFRQH"),
    5: list("JGLDBSTP"),
    6: list("WRTZ"),
    7: list("HQMNSFRJ"),
    8: list("RNFHW"),
    9: list("JZTQPRB"),
}


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            num = int(line.split()[1])
            fromS = int(line.split()[3])
            toS = int(line.split()[5])

            for j in range(num):
                stacks2[toS].append(stacks2[fromS].pop())

    return "".join([stacks2[i][-1] for i in stacks2])


def main2():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            num = int(line.split()[1])
            fromS = int(line.split()[3])
            toS = int(line.split()[5])

            stacks2[toS] += stacks2[fromS][-num:]
            # print(curr)
            stacks2[fromS] = stacks2[fromS][:-num]
            print(stacks2)

            # stacks2[toS].append(stacks2[fromS].pop())

    return "".join([stacks2[i][-1] for i in stacks2])


if __name__ == "__main__":
    # print(main())
    print(main2())
