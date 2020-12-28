n = int(input())

pos_dict = {}
for _ in range(n):
    pos = list(map(int, input().split()))
    if pos[0] not in pos_dict.keys():
        pos_dict[pos[0]] = []
    pos_dict[pos[0]].append(pos[1])

pos_key = pos_dict.keys()
for key in sorted(pos_key):
    for val in sorted(pos_dict[key]):
        print(key, val)
