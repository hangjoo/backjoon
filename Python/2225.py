n, k = map(int, input().split())
cache = [[1 for _ in range(n + 1)] for _ in range(k)]

for k_i in range(1, k):
    for n_i in range(1, n + 1):
        cache[k_i][n_i] = sum(cache[k_i - 1][: n_i + 1])

print(cache[-1][-1] % 1_000_000_000)
