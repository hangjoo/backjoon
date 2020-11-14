num = int(input())
count = 0

while int(num) > 0:
    if float(num) / 2 > int(num / 2):
        count += 1
    num = int(num / 2)
print(count)
