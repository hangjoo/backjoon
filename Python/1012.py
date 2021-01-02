t = int(input())
for _ in range(t):
    m, n, k = list(map(int, input().split()))
    board = [[False for _ in range(m)] for _ in range(n)]
    cabbage_pos = []
    for _ in range(k):
        a, b = list(map(int, input().split()))
        board[b][a] = True
        cabbage_pos.append((a, b))

    count = 0
    while cabbage_pos:
        count += 1
        cabbage_cur = cabbage_pos.pop(0)
        bfs_q = [cabbage_cur]
        board[cabbage_cur[1]][cabbage_cur[0]] = False

        while bfs_q:
            cur_x, cur_y = bfs_q.pop(0)
            if cur_x - 1 >= 0 and board[cur_y][cur_x - 1]:
                bfs_q.append((cur_x - 1, cur_y))
                cabbage_pos.remove((cur_x - 1, cur_y))
                board[cur_y][cur_x - 1] = False
            if cur_x + 1 < m and board[cur_y][cur_x + 1]:
                bfs_q.append((cur_x + 1, cur_y))
                cabbage_pos.remove((cur_x + 1, cur_y))
                board[cur_y][cur_x + 1] = False
            if cur_y - 1 >= 0 and board[cur_y - 1][cur_x]:
                bfs_q.append((cur_x, cur_y - 1))
                cabbage_pos.remove((cur_x, cur_y - 1))
                board[cur_y - 1][cur_x] = False
            if cur_y + 1 < n and board[cur_y + 1][cur_x]:
                bfs_q.append((cur_x, cur_y + 1))
                cabbage_pos.remove((cur_x, cur_y + 1))
                board[cur_y + 1][cur_x] = False

    print(f"{count}")
