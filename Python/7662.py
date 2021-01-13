import sys
import heapq

t = int(sys.stdin.readline())
for _ in range(t):
    q = int(sys.stdin.readline())

    num_status = [False] * 1_000_000
    num_count = 0
    max_heap = []
    min_heap = []
    num_id = 0

    for _ in range(q):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == "I":
            num_status[num_id] = True
            num_count += 1
            heapq.heappush(max_heap, (-num, num_id))
            heapq.heappush(min_heap, (num, num_id))
            num_id += 1
        elif cmd == "D" and num_count > 0:
            if num == 1:
                while max_heap and not num_status[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                pop_num = heapq.heappop(max_heap)
                num_status[pop_num[1]] = False
                num_count -= 1
            elif num == -1:
                while min_heap and not num_status[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                pop_num = heapq.heappop(min_heap)
                num_status[pop_num[1]] = False
                num_count -= 1
    while max_heap and not num_status[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not num_status[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if num_count == 0:
        sys.stdout.write("EMPTY" + "\n")
    else:
        sys.stdout.write(str(-max_heap[0][0]) + " " + str(min_heap[0][0]) + "\n")
