n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]

cases = [[0, 0, 0]]
for i in range(1, n + 1):
    r_cost = min(cases[i - 1][1], cases[i - 1][2]) + costs[i - 1][0]
    g_cost = min(cases[i - 1][0], cases[i - 1][2]) + costs[i - 1][1]
    b_cost = min(cases[i - 1][0], cases[i - 1][1]) + costs[i - 1][2]

    cases.append([r_cost, g_cost, b_cost])

print(min(cases[-1]))
