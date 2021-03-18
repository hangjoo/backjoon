### 문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

### 입출력 예

| numbers | return |
| ------- | ------ |
| "17"    | 3      |
| "011"   | 2      |

### 입출력 예 설명

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

- 11과 011은 같은 숫자로 취급합니다.

### 해설

```python
from itertools import permutations

def check(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5)):
            if num % i == 0:
                return False
        return True
    
def solution(numbers):
    answer = 0
    gen_nums = set()
    
    for i in range(1, len(numbers) + 1):
        for gen_num in [int("".join(val)) for val in permutations(numbers, i)]:
            gen_nums.add(gen_num)
    for gen_num in gen_nums:
        if check(gen_num):
            answer += 1
    
    return answer
```

주어진 숫자 문자열에서 각 숫자를 조합하여 만들 수 있는 수 중 소수인 수의 갯수를 구하는 문제입니다.

먼저 주어진 숫자 문자열의 길이가 N이라고 할 때 N개의 숫자 중 1~N개의 숫자를 조합하여 숫자를 만들 수 있는데, 이를 python의 기본 패키지인 permutations를 사용하여 가능한 숫자 조합을 계산합니다.

이후 집합 자료형인 gen_nums에 조합하여 만들어진 수를 저장하여 중복을 제거하고, 모든 조합의 수를 순회하면서 소수인지 체크하여 소수이면 answer의 값을 1 증가시키는 방법으로 문제를 해결하였습니다.

11과 011은 같은 숫자로 취급하는 것은 두 문자열 모두 int()을 사용하여 형 변환을 거치면 11로 변환되기 때문에 예외처리는 따로 할 필요는 없습니다.