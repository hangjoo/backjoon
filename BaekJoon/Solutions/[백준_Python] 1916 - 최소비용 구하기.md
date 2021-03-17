## 문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

---

## 입력

첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

---

## 출력

첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

---

## 풀이

```python
import sys
from math import inf
from queue import PriorityQueue

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
connect = {node: [] for node in range(1, n + 1)}

for _ in range(m):
    src_node, tgt_node, weight = map(int, sys.stdin.readline().split())
    connect[src_node].append((tgt_node, weight))

src, dst = map(int, sys.stdin.readline().split())

dist = {node: inf for node in range(1, n + 1)}
dist[src] = 0

pq = PriorityQueue()
pq.put([dist[src], src])

while not pq.empty():
    cur_dist, cur_node = pq.get()
    if cur_dist <= dist[cur_node]:
        for node, weight in connect[cur_node]:
            if cur_dist + weight < dist[node]:
                dist[node] = cur_dist + weight
                pq.put([dist[node], node])

sys.stdout.write(str(dist[dst]) + "\n")
```

N개의 도시와 한 도시에서 다른 도시에 도착하는 M개의 버스가 주어졌을 때, 주어진 시작 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력하는 문제입니다.

문제를 보자마자 다익스트라 알고리즘을 사용하는 문제라고 판단하여 해당 알고리즘을 사용하여 구현했습니다. 이 때 시간 제한이 0.5초인데 주어지는 버스의 최대 개수는 100,000개로 100,000개의 입력을 받아야하는 경우가 있으므로 입력하는데 시간을 줄이고자 python의 기본 패키지인 sys를 사용하여 입출력을 처리하도록 하였습니다.

또한 인접행렬을 사용하는 것보다 우선순위 큐를 사용하는 것이 시간 복잡도 측면에서 이점이 있으므로 우선순위 큐를 사용하여 다익스트라 알고리즘을 구현했고 문제 풀이에 성공했습니다.