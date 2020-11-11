num = int(input())
A_set = list(map(int, input().split()))
B_set = list(map(int, input().split()))
A_set.sort()
B_set.sort(reverse=True)

res = 0
for idx in range(num):
    res += A_set[idx] * B_set[idx]

print(res)