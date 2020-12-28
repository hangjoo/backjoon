n, k = list(map(int, input().split()))

n_list = [i for i in range(1, n + 1)]
p_list = []

while n_list:
    for _ in range(k - 1):
        n_list.append(n_list.pop(0))
    p_list.append(n_list.pop(0))

print("<", end="")
for i in range(len(p_list)):
    if i < len(p_list) - 1:
        print(f"{p_list[i]}, ", end="")
    else:
        print(f"{p_list[i]}", end="")
print(">", end="")
