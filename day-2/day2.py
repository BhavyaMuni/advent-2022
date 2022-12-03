e_dict = {"A": 1, "B": 2, "C": 3}
u_dict = {"X": 1, "Y": 2, "Z": 3}
tot = 0
with open("input_day2.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        cur = 0
        e, u = line.split()
        if (e_dict[e] - u_dict[u]) == 1 or (e_dict[e] - u_dict[u]) == -2:
            cur += u_dict[u]
        elif e_dict[e] == u_dict[u]:
            cur += u_dict[u] + 3
        else:
            cur += u_dict[u] + 6

        tot += cur
print(tot)

# part2

e_dict2 = {"A": 1, "B": 2, "C": 3}
u_dict2 = {"X": 0, "Y": 3, "Z": 6}
tot = 0
with open("input_day2.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        cur = 0
        e, u = line.split()
        print(e + " " + u)
        if u == 'X':
            test = e_dict2[e]-1
            if test < 1:
                test = 3
            cur += test + 0
            print(cur)
        elif u == 'Y':
            cur += e_dict2[e] + 3
            print(cur)
        else:
            test = e_dict2[e]+1
            if test > 3:
                test = 1
            cur += test + 6
            print(cur)

        tot += cur
print(tot)
