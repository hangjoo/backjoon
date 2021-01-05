def check(paper):
    flag = paper[0][0]
    for i in paper:
        for j in i:
            if j != flag:
                return -1
    if flag == 1:
        return 1
    else:
        return 0


def cut(paper):
    ret = check(paper)
    if ret == 1:
        return 0, 1
    elif ret == 0:
        return 1, 0
    else:
        pivot = len(paper) // 2
        a = cut([paper[i][:pivot] for i in range(pivot)])
        b = cut([paper[i][pivot:] for i in range(pivot)])
        c = cut([paper[i][:pivot] for i in range(pivot, len(paper))])
        d = cut([paper[i][pivot:] for i in range(pivot, len(paper))])
        return a[0] + b[0] + c[0] + d[0], a[1] + b[1] + c[1] + d[1]


n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

ret = cut(paper)
print(ret[0])
print(ret[1])
