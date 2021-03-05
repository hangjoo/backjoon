from collections import deque

n = int(input())
connect = {node: [] for node in range(1, n + 1)}
for _ in range(n - 1):
    src, tgt, length = map(int, input().split())
    connect[src].append((tgt, length))
    connect[tgt].append((src, length))


# find the farthest node from start node(1).
dist = {node: -1 for node in range(1, n + 1)}
dfs_q = deque()
dfs_q.append(1)
dist[1] = 0

max_node = 1
max_length = 0

while dfs_q:
    cur_node = dfs_q.pop()
    for connect_node, connect_length in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_length
            dfs_q.append(connect_node)
            if dist[connect_node] > max_length:
                max_node = connect_node
                max_length = dist[connect_node]

# re-find the farthest node from max_node.
dist = {node: -1 for node in range(1, n + 1)}
dfs_q = deque()
dfs_q.append(max_node)
dist[max_node] = 0

max_node = 1
max_length = 0

while dfs_q:
    cur_node = dfs_q.pop()
    for connect_node, connect_length in connect[cur_node]:
        if dist[connect_node] == -1:
            dist[connect_node] = dist[cur_node] + connect_length
            dfs_q.append(connect_node)
            if dist[connect_node] > max_length:
                max_node = connect_node
                max_length = dist[connect_node]

print(max_length)
