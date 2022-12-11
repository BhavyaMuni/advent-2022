def main() -> set():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        visited = set()
        directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        h = [0, 0]
        t = [0, 0]
        for line in lines:
            direction, steps = line.split()
            steps = int(steps)
            for i in range(steps):
                h[0] += directions[direction][0]
                h[1] += directions[direction][1]
                dx = t[0] - h[0]
                dy = t[1] - h[1]
                if abs(dx) + abs(dy) >= 3:
                    t[0] += -1 if dx > 0 else 1
                    t[1] += -1 if dy > 0 else 1
                elif abs(dx) > 1:
                    t[0] += -1 if dx > 0 else 1
                elif abs(dy) > 1:
                    t[1] += -1 if dy > 0 else 1

                visited.add((t[0], t[1]))

                # print(f"head: {h}")
                # print(f"tail: {t}")

    print(visited)
    return len(visited)


def main2() -> set():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        visited = set()
        directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
        h = [0, 0]
        t = [0, 0]
        for line in lines:
            direction, steps = line.split()
            steps = int(steps)
            for i in range(steps):
                h[0] += directions[direction][0]
                h[1] += directions[direction][1]
                dx = t[0] - h[0]
                dy = t[1] - h[1]
                if abs(dx) + abs(dy) >= 3:
                    t[0] += -1 if dx > 0 else 1
                    t[1] += -1 if dy > 0 else 1
                elif abs(dx) > 1:
                    t[0] += -1 if dx > 0 else 1
                elif abs(dy) > 1:
                    t[1] += -1 if dy > 0 else 1

                visited.add((t[0], t[1]))

                # print(f"head: {h}")
                # print(f"tail: {t}")

    print(visited)
    return len(visited)


if __name__ == "__main__":
    print(main())
