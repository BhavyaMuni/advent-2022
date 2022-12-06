def main() -> int:
    with open("input.txt", "r") as f:

        line = f.read()

        for i in range(len(line)):
            if len(set(line[i:i+4])) == 4:
                return i+4
    return -1


def main2() -> int:
    with open("input.txt", "r") as f:

        line = f.read()

        for i in range(len(line)):
            if len(set(line[i:i+14])) == 14:
                return i+14
    return -1


if __name__ == "__main__":
    print(main())
    print(main2())
