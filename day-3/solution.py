chars = 'abcdefghijklmnopqrstuvwxyz'
chars = chars + chars.upper()
mapper = {chars[i]: (i+1) for i in range(len(chars))}

with open("input.txt", "r") as f:
    lines = f.readlines()
    tot = 0
    for line in lines:
        part1 = line[:len(line)//2]
        part2 = line[len(line)//2:]

        cha = set(part1).intersection(set(part2)).pop()
        tot += mapper[cha]
        # print(ord(cha.swapcase())-64)

    print(tot)


# part 2


with open("input.txt", "r") as f:
    lines = f.readlines()
    tot = 0
    for k in range(0, len(lines), 3):
        line1 = lines[k]
        line2 = lines[k+1]
        line3 = lines[k+2]

        cha = set(line1).intersection(set(line2).intersection(set(line3)))
        for i in list(cha):
            if i != "\n":
                tot += mapper[i]
        # print(ord(cha.swapcase())-64)

    print(tot)