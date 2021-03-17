## 문제

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

---

## 입력

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

---

## 출력

첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

---

## 풀이

```python
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
```

주어진 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽을 나타낸다고 할 때, 벽을 부술 수 있는 기회가 한 번 주어진 상태에서 (1, 1)에서 (N, M)에 도달하는 최단 경로를 계산하는 문제입니다.

문제에서 키포인트는 벽을 부술 수 있는 기회가 한 번 주어지는 것으로 너비우선탐색(BFS)를 통해 최단경로는 계산할 때 벽을 부술 수 있는지를 나타내는 상태를 함께 큐에 넣어서 최단 경로를 구하고자 했습니다.

그러나 너비우선탐색을 위한 큐에 벽을 부술 수 있는지 여부를 담는 것만으로는 문제를 푸는데 부족합니다.

예를 들어 아래와 같은 맵이 있다고 가정하겠습니다.

0000
0010
0101
1010

(1, 1)에서 출발하여 (2, 4)에서 (3, 4)의 벽을 한번 부수고 (4, 4)에 도달하는 것이 최단경로 7을 구하는 과정입니다. 그러나 (2, 4)에 도착하는 과정에서 (1, 4)에서 (2, 4)로 이동하는 것이 아니라 (2, 3)에서 벽을 한번 부숴 (2, 4)에 도달하는 것이 먼저 탐색되어 최단 경로로 계산되면 (3, 4)의 벽을 부술 수 없게됩니다. 따라서 너비우선탐색을 위한 큐에만 벽을 부술 수 있는지 상태를 나타내는 것이 아니라 추가로 최단 경로를 저장하는 배열에 해당 위치에서 벽을 부수지 않은 상태에서 최단 경로와 벽을 부수고 온 최단 경로를 저장하는 두 가지가 필요합니다.

위와 같은 방법을 통해 (2, 4)에는 벽을 부수고 온 최단 경로와 벽을 부수지 않고 온 최단 경로 두가지가 존재할 수 있고 따라서 벽을 부수지 않고 온 최단 경로를 통해 (3, 4)에 도달할 수 있습니다.

위의 알고리즘을 통해 위 코드처럼 구현하면 문제 풀이에 성공하실 수 있습니다. 주의할 점은 시간 제한이 좀 빠듯하다보니 20번 라인의 if문을 여러 줄에 걸쳐 한다던가 하면 시간 초과가 뜹니다. 먼저 python3가 아닌 pypi로 먼저 채점을 하시고 시간을 줄여보는 것을 추천드립니다.