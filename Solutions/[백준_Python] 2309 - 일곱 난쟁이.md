## 문제

왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

------

## 입력

아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

------

## 출력

일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

------

## 풀이

```
def find(count, ans_list, height_list):
    if count == 7 and sum(ans_list) == 100:
        return True
    elif count > 7 or sum(ans_list) > 100:
        return False
    else:
        for i in range(len(height_list)):
            ans_list.append(height_list[i])
            if find(count + 1, ans_list, height_list[i + 1 :]):
                return True
            else:
                ans_list.pop()
        return False


height_list = []
ans_list = []
for _ in range(9):
    height_list.append(int(input()))

if find(0, ans_list, height_list):
    for i in sorted(ans_list):
        print(i)
```

9가지 원소 중 7개의 원소를 고르는 조합을 찾는 문제 입니다. 경우의 수가 가변적이지 않고 고정이기 때문에 재귀 함수를 사용한 완전 탐색 알고리즘으로 코드를 구현했습니다. 재귀를 호출해가며 ans_list 리스트 변수에 선택한 원소를 넣으며, 재귀가 끝나는 조건에서 문제의 주어진 조건을 만족하면 참, 만족하지 못하면 거짓을 반환하게 하고 재귀를 빠져나와 ans_list의 원소를 정렬시켜 하나씩 출력하도록 구현했습니다.



함수를 구현할 때 처음 인덱스에서 리스트의 끝까지 갈 필요 없이 남아 있는 카운트보다 height_list의 길이가 짧으면 False를 반환하도록 짜서 시간을 더 줄일 수도 있지만 시간제한이 2초라 널널하다 생각하여 생략하였습니다.