nums = []
answer = []


def find(a_num, target, count):
    if count > 8:
        pass
    elif a_num == target:
        answer.append(count)
    else:
        for num in nums:
            if count + len(str(num)) <= 8:
                find(a_num + num, target, count + len(str(num)))
                find(a_num - num, target, count + len(str(num)))
                find(a_num * num, target, count + len(str(num)))
                find(num - a_num, target, count + len(str(num)))
                if num != 0:
                    find(a_num // num, target, count + len(str(num)))
                if a_num != 0:
                    find(num // a_num, target, count + len(str(num)))


def solution(N, number):
    for i in range(1, 9):
        nums.append(int(str(N) * i))

    for num in nums:
        find(num, number, len(str(num)))

    if not answer or min(answer) > 8:
        return -1
    else:
        return min(answer)
