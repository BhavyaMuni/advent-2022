def main() -> int:
    out = 0
    with open("input.txt", "r") as f:
        matrix = [list(i) for i in f.read().splitlines()]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    visible = True
                    temp_i = i + dx
                    temp_j = j + dy

                    while (
                        temp_i >= 0
                        and temp_i < len(matrix)
                        and temp_j >= 0
                        and temp_j < len(matrix[0])
                    ):
                        if matrix[temp_i][temp_j] >= matrix[i][j]:
                            visible = False
                            break
                        temp_i += dx
                        temp_j += dy

                    if visible:
                        print(f"position {i, j} visible {matrix[i][j]}")
                        break

                if visible:
                    out += 1

    return out


def main2() -> int:
    max_score = float("-inf")
    with open("input.txt", "r") as f:
        matrix = [list(i) for i in f.read().splitlines()]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                scenic_score = 1

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    temp_i = i + dx
                    temp_j = j + dy
                    curr_score = 0
                    while (
                        temp_i >= 0
                        and temp_i < len(matrix)
                        and temp_j >= 0
                        and temp_j < len(matrix[0])
                    ):
                        curr_score += 1
                        # print(curr_score)
                        if matrix[temp_i][temp_j] >= matrix[i][j]:
                            break
                        temp_i += dx
                        temp_j += dy

                    scenic_score *= curr_score
                    # print(scenic_score)

                max_score = max(max_score, scenic_score)

    return max_score


if __name__ == "__main__":
    print(main())
    print(main2())
