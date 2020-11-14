x, y, w, h = list(map(int, input().split()))
l, r, d, u = x, w - x, y, h - y
length = [l, r, d, u]
length.sort()
print(length[0])