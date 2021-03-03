## 문제

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

---

## 입력

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

---

## 출력

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

---

## 풀이

```python
from collections import deque

n = int(input())
connect = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    connect[a].append(b)
    connect[b].append(a)

bfs = deque([1])
visit = {i: False for i in range(1, n + 1)}
node = {i: {"p": [], "c": []} for i in range(1, n + 1)}
while bfs:
    cur = bfs.popleft()
    visit[cur] = True
    for i in connect[cur]:
        if not visit[i]:
            node[cur]["c"].append(i)
            node[i]["p"].append(cur)
            bfs.append(i)

for i in range(2, n + 1):
    print(node[i]["p"][-1])
```

주어진 트리에서 노드의 번호 순대로 부모 노드의 번호를 출력하는 문제입니다.



i번 노드와 연결된 노드의 번호들을 connect[i]에 저장하고 너비 우선 탐색(BFS)를 사용하여 루트 노드인 1번 노드부터 순차적으로 탐색하면서 노드들간의 관계를 node 딕셔너리에 저장했습니다. 트리를 탐색하는 과정은 i번째 노드에서 아직 방문하지 않은 노드는 반드시 i번 노드의 자식 노드이므로 해당 노드를 node[i]의 자식으로 저장시키고 해당 자식의 부모 노드를 i로 설정한 뒤에 탐색이 끝나고 2번 노드부터 순차적으로 부모 노드를 출력하여 문제 풀이에 성공했습니다.