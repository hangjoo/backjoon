## 문제

트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

---

## 입력

트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2≤V≤100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. (정점 번호는 1부터 V까지 매겨져 있다고 생각한다)

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

---

## 출력

첫째 줄에 트리의 지름을 출력한다.

---

## 풀이

```python
from collections import deque

v = int(input())
connect = {node: [] for node in range(1, v + 1)}
for _ in range(v):
    line_infos = list(map(int, input().split()))
    src = line_infos[0]
    for i in range(1, len(line_infos) - 1, 2):
        connect[src].append((line_infos[i], line_infos[i + 1]))  # (tgt, cost)


# first dfs.
dist = {node: -1 for node in range(1, v + 1)}
dfs_q = deque()
dfs_q.append(1)
dist[1] = 0

max_node = 1
max_len = 0

while dfs_q:
    cur_node = dfs_q.pop()

    for connect_node, connect_cost in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_cost
            dfs_q.append(connect_node)
            if dist[connect_node] > max_len:
                max_len = dist[connect_node]
                max_node = connect_node

# second dfs.
dist = {node: -1 for node in range(1, v + 1)}
dfs_q = deque()
dfs_q.append(max_node)
dist[max_node] = 0

max_node = 1
max_len = 0

while dfs_q:
    cur_node = dfs_q.pop()

    for connect_node, connect_cost in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_cost
            dfs_q.append(connect_node)
            if dist[connect_node] > max_len:
                max_len = dist[connect_node]
                max_node = connect_node

print(max_len)
```

주어진 트리에서 가장 거리가 먼 두 정점 사이의 거리를 구하는 문제입니다.

똑같은 문제가 [백준 1967 - 트리의 지름]으로 있습니다.

마찬가지로 두 번의 깊이 우선 탐색을 통해 트리의 지름을 쉽게 구할 수 있습니다. 먼저 첫번째 깊이 우선 탐색을 통해 트리의 지름을 구성하는 두 정점 중 하나를 찾아내고, 찾아낸 해당 정점에서 출발하여 다시 한번 깊이 우선 탐색을 통해 가장 먼 정점까지의 거리를 계산하여 트리의 지름을 구할 수 있습니다.

입력 받는 간선의 수의 최대 개수에서 차이가 있어서 다른 알고리즘을 사용해야하는 문제인가 싶었는데 동일하게 구현해서 똑같이 통과한 문제였습니다.