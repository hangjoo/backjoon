n = int(input())
num_list = [int(input()) for _ in range(n)]
max_list = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        max_list[0] = num_list[0]
    elif i == 1:
        max_list[1] = max_list[0] + num_list[1]
    else:
        max_list[i] = max(max_list[i - 3] + num_list[i - 1] + num_list[i], max_list[i - 2] + num_list[i], max_list[i - 1])

print(max_list[-1])
