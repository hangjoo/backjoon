import sys

n = int(sys.stdin.readline())

pos_list = list(map(int, sys.stdin.readline().split()))

idx_list = sorted(set(pos_list))

pressed_list = {}
for i in range(len(idx_list)):
    pressed_list[idx_list[i]] = i

for pos in pos_list:
    sys.stdout.write(str(pressed_list[pos]) + " ")
