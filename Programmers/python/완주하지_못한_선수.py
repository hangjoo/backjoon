# https://programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    table = dict.fromkeys(participant, 0)
    for val in participant:
        table[val] += 1
    for val in completion:
        table[val] -= 1
    for key, val in table.items():
        if val == 1:
            answer = key
            return answer
