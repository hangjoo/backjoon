from math import inf

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    connect = []
    for _ in range(m):
        a, b, k = map(int, input().split())
        connect.append((a, b, k))
        connect.append((b, a, k))
    for _ in range(w):
        a, b, k = map(int, input().split())
        connect.append((a, b, -k))

    def bellman_ford(start_node):
        global n
        dist = {node: inf for node in range(1, n + 1)}
        dist[start_node] = 0

        for _ in range(n - 1):
            for src_node, tgt_node, connect_time in connect:
                if dist[src_node] + connect_time < dist[tgt_node]:
                    dist[tgt_node] = dist[src_node] + connect_time
                if dist[start_node] < 0:
                    return True
        return False

    isBack = False
    for i in range(1, n + 1):
        if bellman_ford(i):
            isBack = True
            break

    if isBack:
        print("YES")
    else:
        print("NO")
