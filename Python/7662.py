import heapq
import sys

t = int(input())
for _ in range(t):
    cmd_num = int(sys.stdin.readline()[:-1])

    min_heap = []
    max_heap = []

    insert_count = 0
    pop_count = 0

    for _ in range(cmd_num):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_heap, (num, num))
            heapq.heappush(max_heap, (-num, num))
            insert_count += 1
        elif cmd == "D" and insert_count > pop_count:
            if num == 1:
                heapq.heappop(max_heap)
                pop_count += 1
            elif num == -1:
                heapq.heappop(min_heap)
                pop_count += 1
            else:
                pass
        else:
            pass

    if insert_count <= pop_count:
        sys.stdout.write("EMPTY\n")
    else:
        sys.stdout.write(str(heapq.heappop(max_heap)[1]) + " " + str(heapq.heappop(min_heap)[1]))
