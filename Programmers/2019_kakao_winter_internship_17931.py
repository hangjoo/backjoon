board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]

moves = [1, 5, 3, 5, 1, 2, 1, 4]

container = [0]

result = 0

for val in moves:
    for i in range(len(board)):
        if board[i][val - 1] != 0:
            if board[i][val - 1] == container[-1]:
                container.pop()
                result += 2
            else:
                container.append(board[i][val - 1])
            board[i][val - 1] = 0
            break
        else:
            continue

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()

print("result :", result)