from queue import Queue

n, m = map(int, input().split())
target = list(map(int, input().split()))
nums = list(range(1, n + 1))
count = 0
for idx, val in target:
    idx_start = nums.index(target[idx])
    idx_end = nums.index(target[idx + 1])
    if (abs(idx_start - idx_end) < n / 2):
        count += abs(idx_start - idx_end)
    else:
        count += n - abs(idx_start - idx_end)
