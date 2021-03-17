from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

shark_eat = 0
shark_size = 2
shark_pos = 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_pos = (i, j)
taken_time = 0

while True:
    bfs_q = deque()
    bfs_q.append(shark_pos)
    fin_flag = True
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    visit[shark_pos[0]][shark_pos[1]] = 0

    while bfs_q:
        cur_i, cur_j = bfs_q.pop()

        if 0 < space[cur_i][cur_j] < shark_size:
            taken_time += visit[cur_i][cur_j]
            space[shark_pos[0]][shark_pos[1]] = 0
            space[cur_i][cur_j] = 9
            shark_pos = (cur_i, cur_j)
            shark_eat += 1
            if shark_eat == shark_size:
                shark_size += 1
                shark_eat = 0
            fin_flag = False
            print(f"baby shark eat {cur_i}{cur_j}")
            print(f"taken time : {visit[cur_i][cur_j]}")
            print(f"space:")
            for row in space:
                for val in row:
                    print(val, end="\t")
                print()
            print(f"visit:")
            for row in visit:
                for val in row:
                    print(val, end="\t")
                print()
            print("==========")
            break

        for a, b in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if (
                0 <= cur_i + a < n
                and 0 <= cur_j + b < n
                and space[cur_i + a][cur_j + b] <= shark_size
                and visit[cur_i + a][cur_j + b] == -1
            ):
                bfs_q.append((cur_i + a, cur_j + b))
                visit[cur_i + a][cur_j + b] = visit[cur_i][cur_j] + 1

    if fin_flag:
        break

print(taken_time)
