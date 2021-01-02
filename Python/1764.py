import sys


def get_key(name: list):
    key = 0
    for num in name:
        key += ord(num)

    return key % 256


n, m = list(map(int, input().split()))
name_list = {i: [] for i in range(256)}

for _ in range(n):
    name = sys.stdin.readline()[:-1]
    name_list[get_key(name)].append(name)

ans_list = []
for _ in range(m):
    name = sys.stdin.readline()[:-1]
    if name in name_list[get_key(name)]:
        ans_list.append(name)

ans_list.sort()
sys.stdout.write(str(len(ans_list)) + "\n")
for name in ans_list:
    sys.stdout.write(str(name) + "\n")
