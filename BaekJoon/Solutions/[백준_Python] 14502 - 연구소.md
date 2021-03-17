## 문제

인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

```
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

```
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

```
2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

---

## 입력

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

---

## 출력

첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

---

## 풀이

```python
from collections import deque
from copy import deepcopy

n, m = list(map(int, input().split()))

board = []
empty_space = deque()
infect_queue = deque()
safe_area = deque()

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 2:
            infect_queue.append((i, j))
        if board[i][j] == 0:
            empty_space.append((i, j))

for a in range(len(empty_space) - 2):
    board[empty_space[a][0]][empty_space[a][1]] = 1
    for b in range(a + 1, len(empty_space) - 1):
        board[empty_space[b][0]][empty_space[b][1]] = 1
        for c in range(b + 1, len(empty_space)):
            board[empty_space[c][0]][empty_space[c][1]] = 1

            cur_board = deepcopy(board)
            cur_queue = deepcopy(infect_queue)
            while cur_queue:
                cur_n, cur_m = cur_queue.popleft()
                if cur_n - 1 >= 0 and cur_board[cur_n - 1][cur_m] == 0:
                    cur_queue.append((cur_n - 1, cur_m))
                    cur_board[cur_n - 1][cur_m] = 2
                if cur_n + 1 < n and cur_board[cur_n + 1][cur_m] == 0:
                    cur_queue.append((cur_n + 1, cur_m))
                    cur_board[cur_n + 1][cur_m] = 2
                if cur_m - 1 >= 0 and cur_board[cur_n][cur_m - 1] == 0:
                    cur_queue.append((cur_n, cur_m - 1))
                    cur_board[cur_n][cur_m - 1] = 2
                if cur_m + 1 < m and cur_board[cur_n][cur_m + 1] == 0:
                    cur_queue.append((cur_n, cur_m + 1))
                    cur_board[cur_n][cur_m + 1] = 2

            area_count = 0
            for row in cur_board:
                area_count += row.count(0)
            safe_area.append(area_count)

            board[empty_space[c][0]][empty_space[c][1]] = 0
        board[empty_space[b][0]][empty_space[b][1]] = 0
    board[empty_space[a][0]][empty_space[a][1]] = 0

print(max(safe_area))
```

바이러스가 퍼져 남는 안전 영역의 수를 구하기 위해 너비 우선 탐색(BFS)를 사용하여 구현하였습니다. 중요한 건 벽을 세우는 경우의 수를 구현하는 것이였는데 입력을 받을 때 따로 벽을 놓을 수 있는 공간을 deque에 저장하여 완전 탐색 알고리즘을 사용하여 3개의 벽을 놓는 경우의 수에 대해 안전 영역의 수를 구해 최댓값을 구하여 문제 풀이에 성공했습니다. 

가로 세로의 최대 길이가 8이었기 때문에 시간 제한 2초에 걸리지 않고 무사히 통과한 것 같습니다.