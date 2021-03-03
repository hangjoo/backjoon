## 문제

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

---

## 입력

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

---

## 출력

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

---

## 풀이

```python
import sys
from math import inf
from queue import PriorityQueue

v, e = list(map(int, sys.stdin.readline().split()))
start = int(input())
connect = {i: [] for i in range(1, v + 1)}
for _ in range(e):
    a, b, w = list(map(int, sys.stdin.readline().split()))
    connect[a].append((b, w))
    

dist = {i: inf for i in range(1, v + 1)}
dist[start] = 0

visit_q = PriorityQueue()
visit_q.put((0, start))

while not visit_q.empty():
    cur_dist, cur_node = visit_q.get()
    if cur_dist <= dist[cur_node]:
        for node, weight in connect[cur_node]:
            if cur_dist + weight < dist[node]:
                dist[node] = cur_dist + weight
                visit_q.put((dist[node], node))

for shortest in dist.values():
    if shortest != inf:
        sys.stdout.write(str(shortest) + "\n")
    else:
        sys.stdout.write("INF" + "\n")
```

방향 그래프와 시작점이 주어졌을 때 다른 모든 정점으로의 최단 경로를 구하는 문제입니다.



먼저 주어지는 간선이 항상 자연수이고 다른 모든 정점으로의 최단 경로를 구하는 문제이기 때문에 다익스트라 알고리즘을 사용하는 문제라고 판단했습니다.



우선순위 큐를 사용한 다익스트라 알고리즘은 시작점부터 출발하여 우선순위 큐에서 뽑아낸 노드에 인접한 노드를 매번 보면서 해당 노드와 시작점과의 현재 최소 거리와 우선순위 큐에서 뽑아낸 노드를 거쳐 해당 노드로 가는 거리를 비교하여 최소 거리에 저장하는 알고리즘입니다. 다익스트라 알고리즘에 대한 자세한 내용은 생략하고 구현 과정을 살펴보겠습니다.



먼저 간선을 저장하는 connect 변수를 생성하는데 이 때 주의할 점은 최대 노드의 수는 20,000개이므로 간선을 노드와 노드 사이의 이차원 행렬로 표현하여 저장하면 20,000^2개, 즉 4억의 저장공간을 필요로 하기 때문에 메모리 초과 오류가 생기게 됩니다. 따라서 노드끼리 이어져 있는 간선만을 저장하도록 인접 리스트 방식을 사용하여 간선을 저장하도록 합니다.



이후로는 각 노드로의 최단 거리를 저장하기 위한 list 변수와 우선순위 큐로 사용할 visit_q를 생성하여 다익스트라 알고리즘을 구현하여 최단 거리를 계산하도록 합니다.



마지막으로 각 노드의 최단 거리를 매 줄에 거쳐 출력하도록 합니다. 코드를 살펴보면 input과 print가 아닌 sys를 사용하여 입출력 처리를 한 것을 볼 수 있습니다. 간선의 최대 개수가 300,000개이다 보니 잦은 입력 출력으로 인해 시간 초과 오류가 떠서 sys.stdin.readline 과 sys.stdout.write을 사용하여 입출력을 처리했습니다.