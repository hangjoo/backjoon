from itertools import permutations


def check(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    answer = 0
    nums = [num for num in numbers]
    gen_nums = set()
    for i in range(1, len(numbers) + 1):
        for gen_num in [int("".join(val)) for val in permutations(nums, i)]:
            gen_nums.add(gen_num)
    for gen_num in gen_nums:
        if check(gen_num):
            answer += 1
            print(gen_num)
    print(gen_nums)

    return answer
