t = int(input())
for _ in range(t):
    n = int(input())
    cache = [0 for _ in range(n)]

    # base nums.
    if n > 0:
        cache[0] = 1
    if n > 1:
        cache[1] = 1
    if n > 2:
        cache[2] = 1
    if n > 3:
        cache[3] = 2
    if n > 4:
        cache[4] = 2

    for i in range(5, n):
        cache[i] = cache[i - 1] + cache[i - 5]

    print(cache[-1])
