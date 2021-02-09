n = int(input())
pibo_num = [1 for _ in range(n)]

for i in range(2, n):
    pibo_num[i] = pibo_num[i - 2] + pibo_num[i - 1]

if n == 0:
    print(0)
else:
    print(pibo_num[-1])
