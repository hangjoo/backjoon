# C. Number of Ways

n = int(input())
nums = list(map(int, input().split()))
cache = [-1 for _ in range(n)]
cache[0] = nums[0]
for i in range(1, n):
    cache[i] = cache[i - 1] + nums[i]

if cache[-1] // 3 != cache[-1] / 3:
    print(0)
elif cache[-1] == 0:
    count_0 = cache[:-1].count(0)
    print(count_0 * (count_0 - 1) // 2)
else:
    count = 0
    idx_1 = []
    idx_2 = []

    for i in range(n - 1):
        if cache[i] == cache[-1] // 3:
            idx_1.append(i)
        if cache[i] == 2 * cache[-1] // 3:
            idx_2.append(i)

    for a in idx_1:
        for b in idx_2:
            if a < b:
                count += 1

    print(count)
