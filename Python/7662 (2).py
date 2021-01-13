import sys
import bisect
from collections import deque

# list에 정렬된 순서로 데이터를 삽입하는 방법으로 bisect 사용.
# 최댓값과 최솟값 삭제시 시간 복잡도의 효율을 위해 deque 사용.
# try, except를 사용하여 딕셔너리에 해당 키가 존재하지 않는지 유무를 파악함.

t = int(sys.stdin.readline())
for _ in range(t):
    num_status = {}
    num_queue = deque()

    q = int(sys.stdin.readline())
    for _ in range(q):
        cmd, num = sys.stdin.readline().split()
        num = int(num)

        if cmd == "I":
            try:
                num_status[num] += 1
            except KeyError:
                num_status[num] = 1
                bisect.insort_left(num_queue, num)
        elif cmd == "D" and num_queue:
            if num == 1:
                if num_status[num_queue[-1]] > 1:
                    num_status[num_queue[-1]] -= 1
                else:
                    del num_status[num_queue[-1]]
                    num_queue.pop()
            elif num == -1:
                if num_status[num_queue[0]] > 1:
                    num_status[num_queue[0]] -= 1
                else:
                    del num_status[num_queue[0]]
                    num_queue.popleft()

    if num_queue:
        sys.stdout.write(str(num_queue[-1]) + " " + str(num_queue[0]) + "\n")
    else:
        sys.stdout.write("EMPTY" + "\n")
