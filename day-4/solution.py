def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        out = 0
        for line in lines:
            int1, int2 = line.split(",")[0], line.split(",")[1]

            int1min, int1max = int(int1.split("-")[0]), int(int1.split("-")[1])
            int2min, int2max = int(int2.split("-")[0]), int(int2.split("-")[1])

            if (int1min >= int2min and int1max <= int2max) or (
                int2min >= int1min and int2max <= int1max
            ):
                out += 1

    return out


def main2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        out = 0
        for line in lines:
            int1, int2 = line.split(",")[0], line.split(",")[1]

            int1min, int1max = int(int1.split("-")[0]), int(int1.split("-")[1])
            int2min, int2max = int(int2.split("-")[0]), int(int2.split("-")[1])

            if (
                (int1min >= int2min and int1min <= int2max)
                or (int1max >= int2min and int1max <= int2max)
                or (int1min >= int2min and int1max <= int2max)
                or (int2min >= int1min and int2max <= int1max)
            ):
                # print(f"{int1min} {int2min}")
                out += 1

    return out


if __name__ == "__main__":
    print(main())
    print(main2())
