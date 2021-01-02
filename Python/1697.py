visit = [-1 for _ in range(100001)]

n, k = list(map(int, input().split()))

if n == k:
    print(0)

cur_pos = n
visit[cur_pos] = 0
bfs_q = [cur_pos]

while bfs_q:
    cur_pos = bfs_q.pop(0)
    if cur_pos - 1 >= 0 and visit[cur_pos - 1] == -1:
        bfs_q.append(cur_pos - 1)
        visit[cur_pos - 1] = visit[cur_pos] + 1
        if cur_pos - 1 == k:
            print(visit[cur_pos - 1])
            break
    if cur_pos + 1 <= 100000 and visit[cur_pos + 1] == -1:
        bfs_q.append(cur_pos + 1)
        visit[cur_pos + 1] = visit[cur_pos] + 1
        if cur_pos + 1 == k:
            print(visit[cur_pos + 1])
            break
    if cur_pos << 1 <= 100000 and visit[cur_pos << 1] == -1:
        bfs_q.append(cur_pos << 1)
        visit[cur_pos << 1] = visit[cur_pos] + 1
        if cur_pos << 1 == k:
            print(visit[cur_pos << 1])
            break
