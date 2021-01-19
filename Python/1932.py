n = int(input())
num_triangle = []
max_triangle = []
for _ in range(n):
    num_row = list(map(int, input().split()))
    num_triangle.append(num_row)
    max_triangle.append([0] * len(num_row))


def max_search(h_idx, w_idx):
    if h_idx == 0:
        return num_triangle[h_idx][0]
    elif w_idx == 0:
        if max_triangle[h_idx][w_idx] == 0:
            max_triangle[h_idx][w_idx] = num_triangle[h_idx][w_idx] + max_search(h_idx - 1, w_idx)
        return max_triangle[h_idx][w_idx]
    elif w_idx == len(num_triangle[h_idx]) - 1:
        if max_triangle[h_idx][w_idx] == 0:
            max_triangle[h_idx][w_idx] = num_triangle[h_idx][w_idx] + max_search(h_idx - 1, w_idx - 1)
        return max_triangle[h_idx][w_idx]
    else:
        if max_triangle[h_idx][w_idx] == 0:
            max_triangle[h_idx][w_idx] = num_triangle[h_idx][w_idx] + max(max_search(h_idx - 1, w_idx - 1), max_search(h_idx - 1, w_idx))
        return max_triangle[h_idx][w_idx]


max_val = []
for i in range(n):
    max_val.append(max_search(n - 1, i))

print(max(max_val))
