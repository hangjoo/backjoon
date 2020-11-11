ax, ay, bx, by, cx, cy = list(map(int, input().split()))

if (ay - by) / (ax - bx) == (ay - cy) / (ax - cx):
    print(-1)

else:
    len_1 = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    len_2 = ((bx - cx) ** 2 + (by - cy) ** 2) ** 0.5
    len_3 = ((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5

    sum_1 = 2 * (len_1 + len_2)
    sum_2 = 2 * (len_2 + len_3)
    sum_3 = 2 * (len_3 + len_1)

    res_1 = max(sum_1, max(sum_2, sum_3))
    res_2 = min(sum_1, min(sum_2, sum_3))
    print(res_1 - res_2)
