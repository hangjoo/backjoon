n, k = list(map(int, input().split()))
items = {i: tuple(map(int, input().split())) for i in range(1, n + 1)}
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i - 1][j - items[i][0]] + items[i][1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])
