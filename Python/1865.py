INF = 123_456_789

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
        dist = {node: INF for node in range(1, n + 1)}
        dist[start_node] = 0

        for _ in range(n - 1):
            for src_node, tgt_node, connect_time in connect:
                if dist[src_node] + connect_time < dist[tgt_node]:
                    dist[tgt_node] = dist[src_node] + connect_time

        for src_node, tgt_node, connect_time in connect:
            # occur renewel dist again.
            if dist[src_node] + connect_time < dist[tgt_node]:
                return True
        return False

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
