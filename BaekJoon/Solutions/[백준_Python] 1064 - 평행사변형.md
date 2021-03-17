## 문제

평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)

이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.

만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.

---

## 입력

첫째 줄에 xA yA xB yB xC yC가 주어진다. 모두 절댓값이 5000보다 작거나 같은 정수이다.

---

## 출력

첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10^-9까지 허용한다.

---

## 풀이

```python
from math import sqrt

ax, ay, bx, by, cx, cy = list(map(int, input().split()))

pos = [[ax, ay], [bx, by], [cx, cy]]
pos = sorted(pos, key=lambda x: x[0])
x_inc = pos[1][0] - pos[0][0]
y_inc = pos[1][1] - pos[0][1]

if (ax - bx) == (ax - cx) == 0 or (ay - by) == (ay - cy) == 0:
    print(-1.0)
elif (ay - by) * (ax - cx) == (ay - cy) * (ax - bx):
    print(-1.0)
else:
    line_1 = sqrt((ay - by) ** 2 + (ax - bx) ** 2)
    line_2 = sqrt((by - cy) ** 2 + (bx - cx) ** 2)
    line_3 = sqrt((cy - ay) ** 2 + (cx - ax) ** 2)

    ret_max = max(line_1 + line_2, line_2 + line_3, line_3 + line_1)
    ret_min = min(line_1 + line_2, line_2 + line_3, line_3 + line_1)
    ret = (ret_max - ret_min) * 2
    print(ret)
```

서로 다른 세 점이 주어졌을 때 가능한 평행사변형의 둘레 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 문제입니다.

평행사변형의 경우 주어진 세 점으로 만들어지는 삼각형의 각 변의 길이를 구한 뒤 두 변을 골라 더해준 뒤 2를 곱하면 쉽게 구할 수 있습니다. 만들 수 없는 평행사변형의 경우 주어진 세 점이 한 직선 위에 놓여 있는 경우인데 12번 라인처럼 x 증가량과 y 증가량을 사용하여 구할 수 있습니다. 이 때 나누기 연산은 소숫점 결과를 반환할 가능성이 크기 때문에 비교시 정확도를 위해 아래와 같은 수식처럼 변형한 뒤 비교하도록 하였습니다.
$$
\frac{y_a-y_b}{x_a-x_b}=\frac{y_a-y_c}{x_a-x_c} \quad \rightarrow \quad (y_a-y_b)(x_a-x_c)=(y_a-y_c)(x_a-x_b)
$$

그러나 이 때 직선이 수직선 혹은 수평선이라면 위 수식 결과가 항상 0이 나오기 때문에 예외의 경우가 발생합니다. 때문에 예외 처리를 위하여 x 증가량이 모두 0이거나 y 증가량이 모두 0인 경우 평행사변형을 만들 수 없다고 출력하도록 처리하여 문제 풀이에 성공했습니다.
