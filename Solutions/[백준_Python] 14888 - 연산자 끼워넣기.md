## 문제

N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

- 1+2+3-4×5÷6
- 1÷2+3+4-5×6
- 1+2÷3×4-5+6
- 1÷2×3-4+5+6

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

- 1+2+3-4×5÷6 = 1
- 1÷2+3+4-5×6 = 12
- 1+2÷3×4-5+6 = 5
- 1÷2×3-4+5+6 = 7

N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

---

## 입력

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

---

## 출력

첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

---

## 풀이

```python
from collections import deque

n = int(input())
nums = deque(map(int, input().split()))
operator = ["+", "-", "*", "/"]
operator_container = [operator[idx] for idx, num in enumerate(list(map(int, input().split()))) for _ in range(num)]

max_num = -1_000_000_000
min_num = 1_000_000_000

# helper function to calculate operator character
def calculate(num_1, num_2, operator):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        if num_1 < 0:
            return -(abs(num_1) // num_2)
        else:
            return num_1 // num_2


def func(cur_num, nums, operators):
    global min_num
    global max_num
    # Base Case
    if len(nums) == 1 and len(operators) == 1:
        final_num = calculate(cur_num, nums[0], operators[0])

        if final_num < min_num:
            min_num = final_num
        if final_num > max_num:
            max_num = final_num
    else:
        for operator in operators:
            # remove operator that used to calculate now.
            next_operators = operators.copy()
            next_operators.remove(operator)
            # hold current operand for next loop.
            next_num = nums.popleft()
            # call recursion.
            func(calculate(cur_num, next_num, operator), nums, next_operators)
            # save holding operand to nums variable.
            nums.appendleft(next_num)


func(nums.popleft(), nums, operator_container)

print(max_num, min_num)

```

주어진 연산자들과 숫자 순서들을 가지고 가능한 최댓값과 최솟값을 구하는 문제입니다. 주어진 숫자들의 최대 길이가 100 이하이므로 완전 탐색 알고리즘을 사용하여 시간 복잡도 $O(n^2)$를 가지더라도 시간 제한 2초 내에 가능할 것이라 생각하여 완전 탐색 알고리즘을 사용하였습니다.

먼저 입력 받은 숫자 순서와 연산자들을 deque와 list를 사용하여 변수에 저장하고 완전 탐색을 위한 func 함수를 정의 했습니다.

func 함수에서는 먼저 최소 문제인 Base Case에 대한 처리로 숫자 순서 배열과 연산자 배열이 길이가 1일 경우 마지막 연산이므로 최종 연산 결과를 계산하여 현재 최댓값과 최솟값보다 각각 크거나 작으면 해당 값으로 바꿔주도록 처리하였습니다.

그리고 부분 문제를 처리하는 부분에서는 연산자 배열에 저장되어있는 연산자들을 모두 순회하면서 현재 연산 결과를 cur_num 변수로 넘기면서 다음 재귀 호출 때엔 사용한 연산자를 제외한 연산자 배열을 넘기면서 모든 경우의 수를 탐색하도록 구현했습니다.