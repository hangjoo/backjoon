n = int(input())

# init
cases = [0 for _ in range(n)]
cases[0] = 1
if n > 1:
    cases[1] = 3

# bottom up DP
for i in range(2, n):
    cases[i] = cases[i - 1] + cases[i - 2] * 2

print(cases[-1] % 10_007)
