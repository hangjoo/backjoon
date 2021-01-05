import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    cmd = int(sys.stdin.readline())
    if cmd != 0:
        heapq.heappush(heap, cmd)
    else:
        if heap:
            sys.stdout.write(str(heapq.heappop(heap)) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
