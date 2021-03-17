## 문제

지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다. 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다. 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

---

## 입력

첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수와 각 파티마다 오는 사람의 수는 모두 0 이상 50 이하의 정수이다.

---

## 출력

첫째 줄에 문제의 정답을 출력한다.

---

## 풀이

```python
from collections import deque

n, m = map(int, input().split())
# a man in true_man must hear Jee-Min's true story.
true_man = deque(map(int, input().split()[1:]))
# people in linked[i] join with i in party.
linked = {i: [] for i in range(1, n + 1)}
# to save party info.
party_list = []
# for bfs.
visit = {i: True if i in true_man else False for i in range(1, n + 1)}

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    party_list.append(party)
    for i in party:
        linked[i].extend(party.copy())
        linked[i].remove(i)

bfs = true_man.copy()
while bfs:
    cur_man = bfs.popleft()
    for i in linked[cur_man]:
        if not visit[i]:
            bfs.append(i)
            visit[i] = True
            true_man.append(i)

count = 0
for party in party_list:
    if not set(party) & set(true_man):
        count += 1

print(count)

```

진실을 아는 사람이 파티에 참가했을 때 지민이는 진실로 말하고, 모르는 사람만 참가한 파티엔 과장되게 이야기를 할 때 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 문제 입니다.

문제에서 고려할 점으로는 예를 들어, 5번이 진실을 아는 사람일 때 3번이 5번과 같은 파티에 참석하면 3번이 참석한 모든 파티에서 지민이는 진실되게 이야기를 해야한다는 점입니다.

이를 염두에 두고 진실을 아는 사람과 같은 파티에 참석했는지 여부를 알기 위해 같은 파티에 참가한 사람끼리 연결할 수 있도록 linked 변수에 저장하여 사용했습니다.

이후 초기 진실을 아는 사람을 가지고 너비 우선 탐색(BFS) 알고리즘을 사용하여 진실된 이야기만 들어야 하는 사람들의 명단을 true_man 변수에 저장했습니다.

탐색이 끝난 후 파티 목록을 다시 순회하면서 집합 자료형의 교집합을 사용하여 파티에 진실을 아는 사람이 없을 경우 카운팅을 1 더하면서 최댓값을 구할 수 있습니다.