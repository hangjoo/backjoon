from queue import PriorityQueue

n, k = map(int, input().split())
dist = [-1 for _ in range(100_001)]

pq = PriorityQueue()
dist[n] = 0
pq.put((dist[n], n))

while not pq.empty():
    cur_dist, cur_pos = pq.get()

    if cur_pos == k:
        print(cur_dist)
        break

    if 2 * cur_pos < 100_001 and dist[2 * cur_pos] == -1:
        dist[2 * cur_pos] = cur_dist
        pq.put((dist[2 * cur_pos], 2 * cur_pos))
    if cur_pos - 1 >= 0 and dist[cur_pos - 1] == -1:
        dist[cur_pos - 1] = cur_dist + 1
        pq.put((dist[cur_pos - 1], cur_pos - 1))
    if cur_pos + 1 < 100_001 and dist[cur_pos + 1] == -1:
        dist[cur_pos + 1] = cur_dist + 1
        pq.put((dist[cur_pos + 1], cur_pos + 1))
