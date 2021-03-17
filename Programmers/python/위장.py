# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clothes_dict = dict()
    for idx in range(len(clothes)):
        if clothes[idx][1] in clothes_dict:
            clothes_dict[clothes[idx][1]] += 1
        else:
            clothes_dict[clothes[idx][1]] = 2

    init_num = 1
    for idx, val in clothes_dict.items():
        init_num *= val

    return init_num - 1
