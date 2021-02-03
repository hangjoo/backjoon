string_a = input()
string_b = input()

lcs = [[0 for _ in range(len(string_b) + 1)] for _ in range(len(string_a) + 1)]

for i, i_chr in enumerate(string_a, 1):
    for j, j_chr in enumerate(string_b, 1):
        if i_chr == j_chr:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[-1][-1])
