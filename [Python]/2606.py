node_num = int(input())
line_num = int(input())
node_dict = {i: list() for i in range(1, node_num + 1)}
visit = [False for _ in range(node_num + 1)]
infect = list()

for _ in range(line_num):
    a, b = list(map(int, input().split()))
    node_dict[a].append(b)
    node_dict[b].append(a)


def dfs(node):
    if node != 1:
        infect.append(node)
    visit[node] = True
    for i in node_dict[node]:
        if visit[i] == False:
            dfs(i)


dfs(1)
print(len(infect))
