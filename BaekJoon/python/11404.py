from math import inf

n = int(input())
m = int(input())
connect = {i: {j: inf for j in range(1, n + 1)} for i in range(1, n + 1)}
for _ in range(m):
    src, dst, cost = map(int, input().split())
    if connect[src][dst] == inf:
        connect[src][dst] = cost
    elif connect[src][dst] > cost:
        connect[src][dst] = cost
dist = connect.copy()
for i in range(1, n + 1):
    dist[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + connect[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + connect[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == inf:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
