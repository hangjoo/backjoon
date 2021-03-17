from math import ceil


def solution(progresses, speeds):
    def get_day(info):
        progress, speed = info
        left_prog = 100 - progress
        return ceil(left_prog / speed)

    taken_days = list(map(get_day, zip(progresses, speeds)))

    answer = []
    cur_day = 0
    for day in taken_days:
        if cur_day >= day:
            answer[-1] += 1
        else:
            answer.append(0)
            answer[-1] += 1
            cur_day = day

    return answer


"""
입력으로 들어온 progresses와 speeds를 사용하여 각 기능이 몇일 뒤에 배포가 가능한지 계산 후에,
해당 배열을 순회하면서 자기가 배포될 때 함께 배포될 수 있는 뒤에 있는 기능을 카운트하여 answer에 저장하여 반환했습니다.
"""
