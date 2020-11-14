# init
boardSize = int(input())
numApple = int(input())

board = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
snakeMove = []

for _ in range(numApple):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1

numMove = int(input())
for _ in range(numMove):
    time, direction = input().split()
    snakeMove.append((int(time), direction))


# snake info.
snakeBody = []  # [[head], ... , [tail]]
snakeDirection = "R"


def _snakeMove(body, direction):
    oldTail = body[0].copy()

    # snake moves.
    for idx in range(len(body)):
        if idx == len(body) - 1:
            if direction == "R":
                body[idx][1] += 1
            elif direction == "L":
                body[idx][1] -= 1
            elif direction == "D":
                body[idx][0] += 1
            else:
                body[idx][0] -= 1
        else:
            body[idx][0] = body[idx + 1][0]
            body[idx][1] = body[idx + 1][1]

    body.insert(0, oldTail)


def _snakeCheck(body):
    head = body[-1]
    if head[0] < 0 or head[0] >= boardSize or head[1] < 0 or head[1] >= boardSize:
        # snake over board.
        return False
    elif board[head[0]][head[1]] == 2:
        # snake conflicts with its body.
        return False
    elif board[head[0]][head[1]] == 1:
        # snake eats an apple.
        board[head[0]][head[1]] = 2
        return True
    else:
        # snake just moves.
        tail = body.pop(0)
        board[head[0]][head[1]] = 2
        board[tail[0]][tail[1]] = 0
        return True


time = 0
snakeBody.append([0, 0])
board[0][0] = 2
while True:
    time += 1
    _snakeMove(snakeBody, snakeDirection)
    if not _snakeCheck(snakeBody):
        print(time)
        break
    else:
        if len(snakeMove) != 0 and time == snakeMove[0][0]:
            if snakeMove[0][1] == "D":
                if snakeDirection == "R":
                    snakeDirection = "D"
                elif snakeDirection == "D":
                    snakeDirection = "L"
                elif snakeDirection == "L":
                    snakeDirection = "U"
                else:
                    snakeDirection = "R"
            else:
                if snakeDirection == "R":
                    snakeDirection = "U"
                elif snakeDirection == "U":
                    snakeDirection = "L"
                elif snakeDirection == "L":
                    snakeDirection = "D"
                else:
                    snakeDirection = "R"
            snakeMove.pop(0)
        else:
            pass
