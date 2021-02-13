n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[-1])
