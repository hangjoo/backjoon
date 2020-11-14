n, m = input().split()
n, m = int(n), int(m)
board = list()
for _ in range(n):
    board.append(list(input()))
min = 50 ** 2
for x in range(0, n - 7):
    for y in range(0, m - 7):
        count = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if ((i + j) % 2 == 0):
                    if (board[x + i][y + j] != board[x][y]):
                        count += 1
                else:
                    if (board[x + i][y + j] == board[x][y]):
                        count += 1
        if (count > 32):
            count = 64 - count
        if (count < min):
            min = count
print(min)
