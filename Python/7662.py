import sys
import heapq

status = {}
max_heap = []
min_heap = []
count = 0

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    for _ in range(k):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(max_heap, (-num, num))
            heapq.heappush(min_heap, num)
            if num not in status.keys():
                status[num] = 0
            status[num] += 1
            count += 1
        else:
            if count == 0:
                continue
            else:
                pop_num = None
                if num == 1:
                    while True:
                        pop_num = heapq.heappop(max_heap)[1]
                        if status[pop_num] > 0:
                            break
                else:
                    while True:
                        pop_num = heapq.heappop(min_heap)
                        if status[pop_num] > 0:
                            break
                status[pop_num] -= 1
                count -= 1
    if count > 0:
        sys.stdout.write(str(heapq.heappop(max_heap)[1]) + " " + str(heapq.heappop(min_heap)) + "\n")
    else:
        sys.stdout.write("EMPTY" + "\n")
