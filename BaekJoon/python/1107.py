n = int(input())
m = int(input())
breaks = []
if m > 0:
    breaks = list(map(int, input().split()))

ret = abs(n - 100)
for num in range(1_000_000):
    check = True
    for num_ in str(num):
        if int(num_) in breaks:
            check = False
            break
    if check:
        press_num = len(str(num)) + abs(n - num)
        if press_num < ret:
            ret = press_num

print(ret)
