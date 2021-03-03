## 문제

nCm을 출력한다.

---

## 입력

n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

---

## 출력

nCm을 출력한다.

---

## 풀이

```python
n, m = list(map(int, input().split()))
cache = [[-1 for j in range(m + 1)] for i in range(n + 1)]


def nCr(n, r):
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1
    else:
        if cache[n][r] == -1:
            cache[n][r] = nCr(n - 1, r) + nCr(n - 1, r - 1)
        return cache[n][r]


print(nCr(n, m))
```

말그대로 nCm을 구하는 문제입니다. 정말 단순하게 알고 있는 nCm 식 그대로 구현했으나 나누기 연산 때문에 오차가 발생하는지 실패...

결국 파스칼의 삼각형 공식을 사용하여 동적계획법(DP)로 해결했습니다.
$$
nCr=n-1Cr+n-1Cr-1
$$
주어진 n과 m 이하에 해당하는 캐시를 저장하기 위해 n개의 행과 m개의 열을 갖는 이차원 배열 캐시를 생성하고 메모이제이션 작업을 수행하면서 nCm을 계산하도록 구현하였습니다.