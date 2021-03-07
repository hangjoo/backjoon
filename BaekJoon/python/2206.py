from collections import deque
from math import inf
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[int(num) for num in sys.stdin.readline().strip()] for _ in range(n)]
dist = [[[inf, inf] for _ in range(m)] for _ in range(n)]

bfs_q = deque()
bfs_q.append((0, 0, 0))  # n_pos, m_pos, isBreak
dist[0][0][0] = 1

while bfs_q:
    cur_n, cur_m, cur_isBreak = bfs_q.popleft()
    if cur_n == n - 1 and cur_m == m - 1:
        break
    for a, b in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        next_n = cur_n + a
        next_m = cur_m + b
        if 0 <= next_n < n and 0 <= next_m < m and dist[next_n][next_m][cur_isBreak] == inf:  # if not visit yet,
            if board[next_n][next_m] == 0:
                dist[next_n][next_m][cur_isBreak] = dist[cur_n][cur_m][cur_isBreak] + 1
                bfs_q.append((next_n, next_m, cur_isBreak))
            if board[next_n][next_m] == 1 and not cur_isBreak:
                dist[next_n][next_m][1] = dist[cur_n][cur_m][cur_isBreak] + 1
                bfs_q.append((next_n, next_m, True))

if dist[-1][-1] == [inf, inf]:
    print(-1)
else:
    print(min(dist[-1][-1]))
