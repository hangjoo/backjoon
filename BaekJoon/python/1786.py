def getPi(p):
    m = len(p)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s, p):
    ans = []
    pi = getPi(p)
    n, m = len(s), len(p)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                ans.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
    return ans


t = input()
p = input()

ret = kmp(t, p)
print(len(ret))
for i in ret:
    print(i + 1)
