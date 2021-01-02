import sys

n = int(sys.stdin.readline())

conference = []
res = []

for _ in range(n):
    start, end = list(map(int, sys.stdin.readline().split()))
    conference.append((start, end))

conference.sort(key=lambda x: x[0])
conference.sort(key=lambda x: x[1])

end_time = 0
count = 0
for s, e in conference:
    if s >= end_time:
        end_time = e
        count += 1

sys.stdout.write(str(count))
