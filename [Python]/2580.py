row_board = {num: [] for num in range(9)}
col_board = {num: [] for num in range(9)}
mini_board = {num: [] for num in range(9)}
blank_q = []

for row in range(9):
    row_line = list(map(int, input().split()))
    row_board[row].extend(row_line)
    for col in range(len(row_line)):
        col_board[col].append(row_line[col])
        if row_line[col] == 0:
            blank_q.append((row, col))
    for col in range(0, len(row_line), 3):
        mini_board[int(row / 3) * 3 + int(col / 3)].extend(row_line[col : col + 3])


def check(check_num, pos_row, pos_col):
    if check_num in row_board[pos_row]:
        return False
    elif check_num in col_board[pos_col]:
        return False
    elif check_num in mini_board[int(pos_row / 3) * 3 + int(pos_col / 3)]:
        return False
    else:
        return True


def search():
    if len(blank_q) != 0:
        pos_row, pos_col = blank_q.pop()
        mini_idx_1 = int(pos_row / 3) * 3 + int(pos_col / 3)
        mini_idx_2 = (pos_row % 3) * 3 + (pos_col % 3)
        for num in range(1, 10):
            if check(num, pos_row, pos_col):
                row_board[pos_row][pos_col] = num
                col_board[pos_col][pos_row] = num
                mini_board[mini_idx_1][mini_idx_2] = num
                if search():
                    return True
                row_board[pos_row][pos_col] = 0
                col_board[pos_col][pos_row] = 0
                mini_board[mini_idx_1][mini_idx_2] = 0
        blank_q.append((pos_row, pos_col))
        return False
    else:
        return True


if __name__ == "__main__":
    if search():
        for row in range(9):
            for col in range(9):
                print(row_board[row][col], end=" ")
            print()