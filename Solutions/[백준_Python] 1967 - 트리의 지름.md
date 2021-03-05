## 문제

트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

![img](source/ttrrtrtr.png)

이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

![img](source/tttttt.png)

트리의 노드는 1부터 n까지 번호가 매겨져 있다.

---

## 입력

파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

---

## 출력

첫째 줄에 트리의 지름을 출력한다.

---

## 풀이

```python
from collections import deque

n = int(input())
connect = {node: [] for node in range(1, n + 1)}
for _ in range(n - 1):
    src, tgt, length = map(int, input().split())
    connect[src].append((tgt, length))
    connect[tgt].append((src, length))


# find the farthest node from start node(1).
dist = {node: -1 for node in range(1, n + 1)}
dfs_q = deque()
dfs_q.append(1)
dist[1] = 0

max_node = 1
max_length = 0

while dfs_q:
    cur_node = dfs_q.pop()
    for connect_node, connect_length in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_length
            dfs_q.append(connect_node)
            if dist[connect_node] > max_length:
                max_node = connect_node
                max_length = dist[connect_node]

# re-find the farthest node from max_node.
dist = {node: -1 for node in range(1, n + 1)}
dfs_q = deque()
dfs_q.append(max_node)
dist[max_node] = 0

max_node = 1
max_length = 0

while dfs_q:
    cur_node = dfs_q.pop()
    for connect_node, connect_length in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_length
            dfs_q.append(connect_node)
            if dist[connect_node] > max_length:
                max_node = connect_node
                max_length = dist[connect_node]

print(max_length)
```

주어진 트리에서 가장 사이의 거리가 먼 두 정점의 거리를 구하는 문제입니다.

가장 먼저 생각난 방법은 깊이 우선 탐색(DFS)를 사용하여 각 정점을 방문하면서 방문한 정점을 하나의 서브 트리의 루트로 보고 해당 서브 트리의 리프 노드의 거리를 계산한 후에 두 합이 최대가 되는 정점을 찾도록 구현했습니다. 그러나 함수의 재귀를 사용하여 깊이 우선 탐색을 구현하다보니 Recursion Error가 발생했습니다. 아무래도 깊이 우선 탐색은 함수의 재귀를 이용해서 구현하면 함수 재귀의 깊이 제한으로 대부분 Recursion Error를 발생시키는 것 같습니다.

두번째로 시도해서 풀이에 성공한 방법은 다음과 같습니다.

먼저 주어진 트리에서 스택을 사용하여 깊이 우선 탐색을 이용해 가장 먼 정점을 찾습니다. 이 때 찾아낸 해당 정점은 트리의 지름의 양 끝점을 구성하는 두 정점 중 하나입니다.

<img src="source/그림1-1614964030892.png" alt="그림1" style="zoom:50%;" />

문제의 예시로 주어진 그래프를 예를 들어보겠습니다. 먼저 주어진 트리의 지름을 구성하는 정점은 9번 정점과 12번 정점입니다. 그 외 다른 정점은 트리의 지름을 사이를 구성하는 정점이거나 해당 정점에서 분기된 정점들 입니다. 이 때 한 정점에서 트리의 지름 양 끝 정점까지의 거리보다 특정 분기된 정점까지의 거리가 멀다면 해당 분기된 정점까지의 거리가 트리의 지름을 구성해야하기 때문에 성립할 수가 없습니다. 따라서 어떤 노드에서든 깊이 우선 탐색을 사용하여 가장 멀리 떨어진 정점을 구한다면 해당 정점이 트리의 지름 양 끝점 중 하나를 구성한다는 것을 알 수 있습니다.

이렇게 트리의 지름 양 끝점 중 한 정점을 구하면 트리의 지름은 해당 정점에서 다시 깊이 우선 탐색을 통해 가장 먼 정점을 구함으로써 구할 수 있습니다. 해당 정점에서 가장 먼 정점이 트리의 지름 양 끝점 중 나머지 한점이라는 것은 당연하기 때문에 최종적으로는 루트 정점에서 깊이 우선 탐색을 통해 가장 먼 정점이자 지름의 양 끝점 중 하나를 구성하는 정점을 구하고 해당 정점에서 깊이 우선 탐색을 통해 가장 먼 정점까지의 거리를 구함으로써 트리의 지름을 구할 수 있게됩니다.

처음에 시도한 방법처럼 서브 트리의 개념으로 접근하면 굉장히 쉽게 풀 수 있다고 느꼈는데 함수 재귀의 한계를 느끼고 다른 방법을 찾느라 오랜 시간이 걸린 문제였습니다.