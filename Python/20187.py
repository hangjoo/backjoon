k = int(input())
cmds = input()
hole_i = int(input())
hole_kinds = [[0, 0], [0, 1], [1, 0], [1, 1]]

row_i = [[i, False] for i in range(2 ** k)]
col_i = [[i, False] for i in range(2 ** k)]

row_cmd = []
col_cmd = []
for cmd in cmds:
    if cmd == "R":
        col_cmd.append(False)
    elif cmd == "L":
        col_cmd.append(True)
    elif cmd == "U":
        row_cmd.append(True)
    elif cmd == "D":
        row_cmd.append(False)


def fold(list_i, cmds):
    if len(list_i) > 1:
        ret = []
        cmd = cmds.pop(0)
        if cmd == False:
            list_i[: len(list_i) // 2] = list(map(lambda x: [x[0], not x[1]], list_i[: len(list_i) // 2]))
            ret.extend(fold(list_i[: len(list_i) // 2], list(map(lambda x: not x, cmds))))
            ret.extend(fold(list_i[len(list_i) // 2 :], cmds.copy()))
        elif cmd == True:
            list_i[len(list_i) // 2 :] = list(map(lambda x: [x[0], not x[1]], list_i[len(list_i) // 2 :]))
            ret.extend(fold(list_i[: len(list_i) // 2], cmds.copy()))
            ret.extend(fold(list_i[len(list_i) // 2 :], list(map(lambda x: not x, cmds))))
        return ret
    else:
        return list_i


row_ret = fold(row_i, row_cmd)
col_ret = fold(col_i, col_cmd)

for row_idx in row_ret:
    for col_idx in col_ret:
        hole_ret = hole_kinds[hole_i].copy()
        if row_idx[1]:
            hole_ret[0] = not hole_ret[0]
        if col_idx[1]:
            hole_ret[1] = not hole_ret[1]
        print(hole_kinds.index(hole_ret), end=" ")
    print()
