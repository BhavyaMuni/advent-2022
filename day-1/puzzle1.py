max_o = -1
with open("input_1.txt", "r") as f:
    lines = f.readlines()
    cur = 0
    for l in lines:
        if l.strip():
            cur += int(l)
        else:
            max_o = max(max_o, cur)
            cur = 0
print(max_o)

# part2
max_o = []
with open("input_1.txt", "r") as f:
    lines = f.readlines()
    cur = 0
    for l in lines:
        if l.strip():
            cur += int(l)
        else:
            max_o.append(cur)
            cur = 0
print(sorted(max_o)[-1] + sorted(max_o)[-2] + sorted(max_o)[-3])
