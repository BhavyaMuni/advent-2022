from collections import defaultdict
# def main():
#     all_dirs = []
#     out = 0
#     with open("input.txt", "r") as f:
#         lines = f.readlines()
#         for i in lines:
#             if "dir " in i:
#                 _, n = i.split()
#                 all_dirs.append(n)
#         # print(lines)
#         sub_dirs = {k: [] for k in all_dirs}
#         dir_totals = {k: 0 for k in all_dirs}
#         for i in all_dirs:
#             x = lines.index(f"$ cd {i}\n")
#             if lines[x+1] == "$ ls\n":
#                 k = x+2
#                 while k < len(lines) and lines[k][0] != "$":
#                     if "dir " in lines[k]:
#                         _, sub_name = lines[k].split()
#                         sub_dirs[i].append(sub_name)
#                     else:
#                         fsize, _ = lines[k].split()
#                         dir_totals[i] += int(fsize)
#                     k += 1
#         print(sub_dirs)

#         for x in sub_dirs:
#             for a in sub_dirs[x]:
#                 dir_totals[x] += dir_totals[a]
        
#         for i in dir_totals:
#             if dir_totals[i] <= 100000:
#                 print(i, dir_totals[i])
#                 out += dir_totals[i]
            
#     return out


def new_main():

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        dir_totals = defaultdict(int)
        curr_dir = ""
        parent_dir = []
        for x, i in enumerate(lines):
            if i[0] == "$":
                if i == "$ cd ..":
                    ix = curr_dir[::-1].index("/", 1)
                    parent_dir.pop()
                    curr_dir = "".join(curr_dir[:-ix])
                elif i == "$ ls":
                    pass
                else:
                    parent_dir.append(curr_dir)
                    curr_dir += i.split()[2] + "/"
            else:
                if "dir " in i:
                    pass
                else:
                    size = int(i.split()[0])
                    dir_totals[curr_dir] += size
                    for i in parent_dir:
                        dir_totals[i] += size
            # print(curr_dir)
        out = 0
        for i in dir_totals:
            if dir_totals[i] < 100000:
                print(i, dir_totals[i])
                out += dir_totals[i]

    return out


if __name__ == "__main__":
    # print(main())
    print(new_main())
