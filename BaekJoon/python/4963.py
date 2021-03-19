from collections import deque

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    islands = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                islands.append((i, j))

    islands_count = 0

    while islands:
        islands_count += 1
        pivot_i, pivot_j = islands.pop()

        visit = [[False for _ in range(w)] for _ in range(h)]
        visit[pivot_i][pivot_j] = True

        bfs_q = deque()
        bfs_q.append((pivot_i, pivot_j))

        while bfs_q:
            cur_i, cur_j = bfs_q.popleft()

            for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                next_i = cur_i + i
                next_j = cur_j + j
                if 0 <= next_i < h and 0 <= next_j < w and not visit[next_i][next_j] and board[next_i][next_j] == 1:
                    visit[next_i][next_j] = True
                    islands.remove((next_i, next_j))
                    bfs_q.append((next_i, next_j))

    print(islands_count)
