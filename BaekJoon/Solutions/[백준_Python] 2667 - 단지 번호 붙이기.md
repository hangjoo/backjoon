## 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

![img](https://blog.kakaocdn.net/dn/270X4/btqUfZG9T5c/oLdIcOtOWCDiRB5Ws2LAn0/img.png)

------

## 입력

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

------

## 출력

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

------

## 풀이

```
from collections import deque

n = int(input())

board = [[] for _ in range(n)]
house = deque()
visit_num = []

for i in range(n):
    line = input()
    for j in range(n):
        board[i].append(int(line[j]))
        if board[i][j] == 1:
            house.append((i, j))

while house:
    visit_q = deque()
    visit_q.append(house.popleft())
    visit_count = 0

    while visit_q:
        cur_i, cur_j = visit_q.popleft()
        board[cur_i][cur_j] = 0
        visit_count += 1

        if cur_i - 1 >= 0 and board[cur_i - 1][cur_j] == 1:
            visit_q.append((cur_i - 1, cur_j))
            board[cur_i - 1][cur_j] = 0
            house.remove((cur_i - 1, cur_j))
        if cur_i + 1 < n and board[cur_i + 1][cur_j] == 1:
            visit_q.append((cur_i + 1, cur_j))
            board[cur_i + 1][cur_j] = 0
            house.remove((cur_i + 1, cur_j))
        if cur_j - 1 >= 0 and board[cur_i][cur_j - 1] == 1:
            visit_q.append((cur_i, cur_j - 1))
            board[cur_i][cur_j - 1] = 0
            house.remove((cur_i, cur_j - 1))
        if cur_j + 1 < n and board[cur_i][cur_j + 1] == 1:
            visit_q.append((cur_i, cur_j + 1))
            board[cur_i][cur_j + 1] = 0
            house.remove((cur_i, cur_j + 1))

    visit_num.append(visit_count)

print(len(visit_num))
for count in sorted(visit_num):
    print(count)
```

연결된 집의 모임인 단지의 영역 갯수와 영역의 넓이를 차례로 출력하는 문제입니다.

영역의 넓이는 너비 우선 탐색(BFS)를 사용하여 구현했으며, 처음 입력 받을 때 집의 좌표를 deque를 사용해 house 변수에 저장하고 매번 집을 방문할 때마다 해당 좌표를 house 변수에서 삭제하는 방법을 통해 아직 단지에 속하지 않는 집의 좌표를 구하도록 구현하였습니다.

리스트를 사용하여 너비 우선 탐색과 집의 좌표를 구하는 큐를 구현할 수 있지만, 리스트보다 deque를 사용하는 것이 시간복잡도 측면에서 이점을 가지므로 deque를 사용하여 구현했습니다.