n = int(input())
days = [list(map(int, input().split())) for _ in range(n)]
max_profit = [0 for _ in range(n)]

if days[0][0] <= n:
    max_profit[0 + days[0][0] - 1] = days[0][1]
for i in range(1, n):
    max_profit[i] = max(max_profit[i - 1], max_profit[i])
    if i + days[i][0] - 1 < n:
        do_appointment = i + days[i][0] - 1
        max_profit[do_appointment] = max(max_profit[i - 1] + days[i][1], max_profit[do_appointment])

print(max_profit[-1])
