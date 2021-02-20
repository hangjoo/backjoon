t = int(input())
for _ in range(t):
    n = int(input())

    count = [0, 0, 0, 0, 0]

    count[0] += n // 60

    n = n % 60

    def get_count(n):
        count = [0, 0, 0]  # 10, 1, -1
        count[0] += n // 10
        if n % 10 <= 5:
            count[1] += n % 10
        else:
            count[0] += 1
            count[2] += 10 - n % 10

        return count

    if n <= 35:
        ret = get_count(n)
        count[1] += ret[0]
        count[3] += ret[1]
        count[4] += ret[2]
    else:
        ret = get_count(60 - n)
        count[0] += 1
        count[2] += ret[0]
        count[3] += ret[2]
        count[4] += ret[1]

    print(*count)
