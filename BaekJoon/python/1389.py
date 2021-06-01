from math import inf

n, m = map(int, input().split())

w = [[inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    w[a][b] = 1
    w[b][a] = 1

# use floyd-warshall
for m in range(n):
    for s in range(n):
        for e in range(n):
            if w[s][m] + w[m][e] < w[s][e]:
                w[s][e] = w[s][m] + w[m][e]

min_count = inf
min_man = inf
for i in range(n):
    kevin_count = 0
    for j in range(n):
        if i != j:
            kevin_count += w[i][j]
    if kevin_count < min_count:
        min_count = kevin_count
        min_man = i

print(min_man + 1)
