import sys

n, m = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        nums_sum[x][y] = nums[x - 1][y - 1] + nums_sum[x - 1][y] + nums_sum[x][y - 1] - nums_sum[x - 1][y - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ret = nums_sum[x2][y2] - nums_sum[x1 - 1][y2] - nums_sum[x2][y1 - 1] + nums_sum[x1 - 1][y1 - 1]
    sys.stdout.write(str(ret) + "\n")

print(nums_sum)