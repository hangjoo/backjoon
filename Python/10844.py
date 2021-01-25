n = int(input())

count = [[-1 for _ in range(10)] for _ in range(n)]
count[0] = [1 for _ in range(10)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            count[i][0] = count[i - 1][1]
        elif j == 9:
            count[i][9] = count[i - 1][8]
        else:
            count[i][j] = count[i - 1][j - 1] + count[i - 1][j + 1]

print(sum(count[n - 1][1:]) % 1_000_000_000)
