num = input().split()
sum = 0
for i in num:
    sum += int(i) ** 2
print(sum % 10)
