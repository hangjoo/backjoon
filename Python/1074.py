def func(x_idx, y_idx, target, start_value):
    if target[0] in range(x_idx[0], x_idx[1]) and target[1] in range(y_idx[0], y_idx[1]):
        if x_idx[0] == x_idx[1] - 1 and y_idx[0] == y_idx[1] - 1:
            print(start_value)
        else:
            x_pivot = (x_idx[1] + x_idx[0]) // 2
            y_pivot = (y_idx[1] + y_idx[0]) // 2
            strides = (x_idx[1] - x_idx[0]) * (y_idx[1] - y_idx[0]) // 4
            func([x_idx[0], x_pivot], [y_idx[0], y_pivot], target, start_value)
            func([x_pivot, x_idx[1]], [y_idx[0], y_pivot], target, start_value + strides * 1)
            func([x_idx[0], x_pivot], [y_pivot, y_idx[1]], target, start_value + strides * 2)
            func([x_pivot, x_idx[1]], [y_pivot, y_idx[1]], target, start_value + strides * 3)


n, r, c = list(map(int, input().split()))
func([0, 2 ** n], [0, 2 ** n], [c, r], 0)
