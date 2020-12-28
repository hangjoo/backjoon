n, k = list(map(int, input().split()))

save = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]


def combination(n, k):
    if save[n][k] > -1:
        return save[n][k]
    else:
        if k == 0 or k == n:
            save[n][k] = 1
        else:
            save[n][k] = combination(n - 1, k - 1) + combination(n - 1, k)
        return save[n][k]


print(combination(n, k))