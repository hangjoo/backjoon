array = [[int(i) for i in input()] for _ in range(10)]

row_pos = []
row_max = 0
col_pos = []
col_max = 0
for i in range(10):
    for j in range(10):
        if array[i][j] == 1:
            pos = [i, j]
            row_len = 1
            col_len = 1
            for j2 in range(j + 1, 10):
                if array[i][j2] == 1:
                    row_len += 1
                if row_len > row_max:
                    row_max = row_len
                    row_pos = pos
            for i2 in range(i + 1, 10):
                if array[i2][j] == 1:
                    col_len += 1
                if col_len > col_max:
                    col_max = col_len
                    col_pos = pos


def check(array, row_pos, col_pos, row_max, col_max):
    if row_max == col_max:
        if row_pos[0] == col_pos[0] and row_pos[1] == col_pos[1]:
            for i in range(col_max):
                for j in range(row_max - i):
                    if array[row_pos[0] + i][row_pos[1] + j] != 1:
                        return -1
            return [[row_pos[0], row_pos[1]], [row_pos[0], row_pos[1] + row_max - 1], [row_pos[0] + col_max - 1, row_pos[1]]]
        if (row_pos[1] + row_max - 1) == col_pos[1] and row_pos[0] == col_pos[0]:
            for i in range(col_max):
                for j in range(i, row_max):
                    if array[row_pos[0] + i][row_pos[1] + j] != 1:
                        return -1
            return [[row_pos[0], row_pos[1]], [row_pos[0], row_pos[1] + row_max - 1], [row_pos[0] + col_max - 1, row_pos[1] + row_max - 1]]
        if row_pos[1] == col_pos[1] and row_pos[0] == (col_pos[0] + col_max - 1):
            for i in range(col_max):
                for j in range(i + 1):
                    if array[col_pos[0] + i][col_pos[1] + j] != 1:
                        return -1
            return [[col_pos[0], col_pos[1]], [col_pos[0] + col_max - 1, col_pos[1]], [col_pos[0] + col_max - 1, col_pos[1] + row_max - 1]]
        if (row_pos[1] + row_max - 1) == col_pos[1] and row_pos[0] == (col_pos[0] + col_max - 1):
            for i in range(col_max):
                for j in range(row_max - i - 1, row_max):
                    if array[col_pos[0] + i][row_pos[1] + j] != 1:
                        return -1
            return [[col_pos[0], col_pos[1]], [row_pos[0], row_pos[1]], [col_pos[0] + col_max - 1, col_pos[1]]]
    else:
        if row_max % 2 == 1 and row_max // 2 + 1 == col_max:
            if (row_pos[1] + row_max // 2) == col_pos[1] and row_pos[0] == col_pos[0]:
                for i in range(col_max):
                    for j in range(-col_max + i + 1, col_max - i):
                        if array[col_pos[0] + i][col_pos[1] + j] != 1:
                            return -1
                return [[row_pos[0], row_pos[1]], [row_pos[0], row_pos[1] + row_max - 1], [col_pos[0] + col_max - 1, col_pos[1]]]
            if (row_pos[1] + row_max // 2) == col_pos[1] and row_pos[0] == (col_pos[0] + col_max - 1):
                for i in range(col_max):
                    for j in range(-i, i + 1):
                        if array[col_pos[0] + i][col_pos[1] + j] != 1:
                            return -1
                return [[col_pos[0], col_pos[1]], [row_pos[0], row_pos[1]], [row_pos[0], row_pos[1] + row_max - 1]]
        if col_max % 2 == 1 and row_max == col_max // 2 + 1:
            if (col_pos[0] + col_max // 2) == row_pos[0] and col_pos[1] == row_pos[1]:
                for j in range(row_max):
                    for i in range(-row_max + j + 1, row_max - j):
                        if array[row_pos[0] + i][row_pos[1] + j] != 1:
                            return -1
                return [[col_pos[0], col_pos[1]], [row_pos[0], row_pos[1] + row_max - 1], [col_pos[0] + col_max - 1, col_pos[1]]]
            if (col_pos[0] + col_max // 2) == row_pos[0] and col_pos[1] == (row_pos[1] + row_max - 1):
                for j in range(row_max):
                    for i in range(-j, j + 1):
                        if array[row_pos[0] + i][row_pos[1] + j] != 1:
                            return -1
                return [[col_pos[0], col_pos[1]], [row_pos[0], row_pos[1]], [col_pos[0] + col_max - 1, col_pos[1]]]
    return -1


if row_max == 0 or col_max == 0:
    print(0)
else:
    ret = check(array, row_pos, col_pos, row_max, col_max)
    if ret == -1:
        print(0)
    else:
        for pos in ret:
            print(pos[0] + 1, pos[1] + 1)
