n = int(input())
seq = [0] + list(map(int, input().split()))

cases = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i):
        if seq[j] < seq[i] and cases[j] + seq[i] > cases[i]:
            cases[i] = cases[j] + seq[i]

print(max(cases))
