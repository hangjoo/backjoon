# https://programmers.co.kr/learn/courses/30/lessons/42747#


def solution(citations):
    answer = 0
    sorted_citations = sorted(citations)
    count = {i: 0 for i in range(len(sorted_citations) + 1)}

    # for key in count.keys():
    #     for val in sorted_citations:
    #         if key <= val:
    #             count[key] += 1

    for key in count.keys():
        count[key] += len(list(filter(lambda x: key <= x, sorted_citations)))

    for key, val in count.items():
        if key <= val:
            answer = key

    return answer


"""
i번 이상 인용된 논문의 갯수를 count[i]에 저장시키는 딕셔너리를 생성하고,
논문 리스트를 순회하면서 count[i]에 해당 값을 저장시켜줬습니다.
그리고나서 i번 이상 인용된 논문이 i편 이상인 i의 최댓값을 구해서 H-index를 구했습니다.
그리고 중간에 filter를 사용해서 파이써닉하게 한번 해봤습니다..
"""
