import sys

n, m = list(map(int, sys.stdin.readline().split()))
connect = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    connect[a].append(b)
    connect[b].append(a)

component_set = []
for start in range(1, n + 1):
    pass_flag = False
    for component in component_set:
        if start in component:
            pass_flag = True
            break
    if not pass_flag:
        component = []
        visit = {i: False for i in range(1, n + 1)}
        bfs = [start]
        visit[start] = True
        while bfs:
            cur = bfs.pop(0)
            component.append(cur)
            for target in connect[cur]:
                if not visit[target]:
                    bfs.append(target)
                    visit[target] = True
        component.sort()
        if component not in component_set:
            component_set.append(component)

sys.stdout.write(str(len(component_set)))
