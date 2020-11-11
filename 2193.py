def func(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    else:
        if save[idx - 1] == -1:
            save[idx - 1] = func(idx - 1)
        if save[idx - 2] == -1:
            save[idx - 2] = func(idx - 2)
        num1 = save[idx - 1]
        num2 = save[idx - 2]
        return num1 + num2


N = int(input())
save = [-1 for _ in range(N)]

print(func(N))
