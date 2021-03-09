from collections import deque

v = int(input())
connect = {node: [] for node in range(1, v + 1)}
for _ in range(v):
    line_infos = list(map(int, input().split()))
    src = line_infos[0]
    for i in range(1, len(line_infos) - 1, 2):
        connect[src].append((line_infos[i], line_infos[i + 1]))  # (tgt, cost)


# first dfs.
dist = {node: -1 for node in range(1, v + 1)}
dfs_q = deque()
dfs_q.append(1)
dist[1] = 0

max_node = 1
max_len = 0

while dfs_q:
    cur_node = dfs_q.pop()

    for connect_node, connect_cost in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_cost
            dfs_q.append(connect_node)
            if dist[connect_node] > max_len:
                max_len = dist[connect_node]
                max_node = connect_node

# second dfs.
dist = {node: -1 for node in range(1, v + 1)}
dfs_q = deque()
dfs_q.append(max_node)
dist[max_node] = 0

max_node = 1
max_len = 0

while dfs_q:
    cur_node = dfs_q.pop()

    for connect_node, connect_cost in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_cost
            dfs_q.append(connect_node)
            if dist[connect_node] > max_len:
                max_len = dist[connect_node]
                max_node = connect_node

print(max_len)
