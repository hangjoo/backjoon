from math import sqrt

t = int(input())
for _ in range(t):
    x, y = list(map(int, input().split()))
    diff = y - x
    # rounding off the decimal point of the square root.
    round_sqrt = int(sqrt(diff))

    # if the differnce is square number,
    if round_sqrt ** 2 == diff:
        print(2 * round_sqrt - 1)
    else:
        # if diff is closer to square of round_sqrt than squar of (round_sqrt + 1)
        if diff - (round_sqrt ** 2) < (round_sqrt + 1) ** 2 - diff:
            print(2 * round_sqrt)
        else:
            print(2 * round_sqrt + 1)
