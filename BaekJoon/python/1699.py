n = int(input())

cases = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for base_num in range(1, int(i ** 0.5) + 1):
        if cases[i - base_num * base_num] + 1 < cases[i]:
            cases[i] = cases[i - base_num * base_num] + 1

print(cases[-1])
