str1, str2 = list(input().split())

len1 = len(str1)
len2 = len(str2)  # len2 > len1

min = 50
for i in range(len2 - len1 + 1):
    dif = 0
    for j in range(len1):
        if str1[j] != str2[i + j]:
            dif += 1

    if dif < min:
        min = dif

print(min)
