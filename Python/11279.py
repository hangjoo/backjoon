import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        if heap:
            sys.stdout.write(str(heapq.heappop(heap)[1]) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
    else:
        heapq.heappush(heap, (-cmd, cmd))
