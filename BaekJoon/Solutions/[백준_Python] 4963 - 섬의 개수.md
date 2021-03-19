## 문제

정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

![img](https://www.acmicpc.net/upload/images/island.png)

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

---

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

---

## 출력

각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

---

## 풀이

```python
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
```

주어진 지도에서 땅이 가로, 세로 또는 대각선으로 연결될 수 있다고 할 때 연결된 땅들을 하나의 섬이라고 보고 섬의 개수를 출력하는 문제입니다.

임의의 땅에서 출발하여 너비 우선 탐색(BFS) 혹은 깊이 우선 탐색(DFS)를 탐색하여 이어진 땅들을 방문하고 이렇게 이어진 땅들을 하나의 섬으로 계산한 뒤 이 과정을 방문하지 않은 땅에 대해 반복함으로써 최종적으로 주어진 지도의 섬의 개수를 구할 수 있게 됩니다.

먼저 지도의 가로와 세로 길이, 그리고 지도의 정보를 입력받습니다. 그리고 지도에 존재하는 땅들의 좌표를 islands 배열에 (i, j) 형태로 저장합니다. 그리고 islands 배열에서 땅의 좌표를 하나 뽑아 해당 땅에서부터 시작하여 이어진 땅들을 너비 우선 탐색을 사용하여 방문합니다. 방문한 땅들은 시작한 땅과 이어져 있기 때문에 islands 배열에서도 삭제해줍니다. 이렇게 한번의 너비 우선 탐색이 끝나면 시작한 땅과 이어진 모든 땅들은 islands 배열에서 제거되고 islands 배열에는 아직 방문하지 않은, 즉 다른 섬으로 존재하는 땅들의 좌표가 남아있습니다. 따라서 앞선 과정이 islands에 땅의 좌표가 남지 않을 때까지 반복하고, 이렇게 반복한 횟수가 지도에 존재하는 섬의 개수임을 알 수 있습니다.