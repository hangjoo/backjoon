def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i

    return res


test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split()))
    res_a = factorial(m)
    res_b = factorial(n)
    res_c = factorial(m - n)
    print(int(res_a / (res_b * res_c)))
