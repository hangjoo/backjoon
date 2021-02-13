n = int(input())
pos_list = [list(map(int, input().split())) for _ in range(n // 2)]
max_x = 0
max_y = 0
for pos in pos_list:
    for i in range(0, 3, 2):
        if pos[i] == 1 or pos[i] == 2:
            if pos[i + 1] > max_x:
                max_x = pos[i + 1]
        if pos[i] == 3 or pos[i] == 4:
            if pos[i + 1] > max_y:
                max_y = pos[i + 1]
max_x += 1
max_y += 1


def pos_tranpose(pos_list, max_x, max_y):
    new_pos_list = []
    for pos in pos_list:
        new_pos = []
        for i in range(0, 3, 2):
            if pos[i] == 1:
                new_pos.append(pos[i + 1])
            if pos[i] == 2:
                new_pos.append(2 * max_x + max_y - pos[i + 1])
            if pos[i] == 3:
                new_pos.append(2 * max_x + 2 * max_y - pos[i + 1])
            if pos[i] == 4:
                new_pos.append(max_x + pos[i + 1])
        new_pos_list.append(new_pos)
    return new_pos_list


def check(a1_pos, a2_pos, b1_pos, b2_pos):
    start_pos = min(a1_pos, a2_pos)
    end_pos = max(a1_pos, a2_pos)
    if b1_pos in range(start_pos, end_pos) and b2_pos not in range(start_pos, end_pos):
        return True
    if b1_pos not in range(start_pos, end_pos) and b2_pos in range(start_pos, end_pos):
        return True
    return False


pos_list = pos_tranpose(pos_list, max_x, max_y)
count_1 = 0
count_2 = 0
for src_pos in pos_list:
    cur_count = 0
    for tgt_pos in pos_list:
        if src_pos != tgt_pos:
            if check(src_pos[0], src_pos[1], tgt_pos[0], tgt_pos[1]):
                count_1 += 1
                cur_count += 1
    if cur_count > count_2:
        count_2 = cur_count

print(count_1 // 2)
print(count_2)
