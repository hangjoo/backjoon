from collections import deque

n, m = map(int, input().split())
# a man in true_man must hear Jee-Min's true story.
true_man = deque(map(int, input().split()[1:]))
# people in linked[i] join with i in party.
linked = {i: [] for i in range(1, n + 1)}
# to save party info.
party_list = []
# for bfs.
visit = {i: True if i in true_man else False for i in range(1, n + 1)}

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    party_list.append(party)
    for i in party:
        linked[i].extend(party.copy())
        linked[i].remove(i)

bfs = true_man.copy()
while bfs:
    cur_man = bfs.popleft()
    for i in linked[cur_man]:
        if not visit[i]:
            bfs.append(i)
            visit[i] = True
            true_man.append(i)

count = 0
for party in party_list:
    if not set(party) & set(true_man):
        count += 1

print(count)
