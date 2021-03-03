## 문제

이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

![img](source/trtr.png)

예를 들어 위와 같은 이진 트리가 입력되면,

- 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
- 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
- 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

가 된다.

---

## 입력

첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

---

## 출력

첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

---

## 풀이

```python
n = int(input())
nodes = {}
for _ in range(n):
    m_node, l_node, r_node = input().split()
    nodes[m_node] = {"left": l_node, "right": r_node}


def preorder(node):
    print(node, end="")
    if nodes[node]["left"] != ".":
        preorder(nodes[node]["left"])
    if nodes[node]["right"] != ".":
        preorder(nodes[node]["right"])


def inorder(node):
    if nodes[node]["left"] != ".":
        inorder(nodes[node]["left"])
    print(node, end="")
    if nodes[node]["right"] != ".":
        inorder(nodes[node]["right"])


def postorder(node):
    if nodes[node]["left"] != ".":
        postorder(nodes[node]["left"])
    if nodes[node]["right"] != ".":
        postorder(nodes[node]["right"])
    print(node, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
print()
```

주어진 트리를 전위 탐색, 중위 탐색, 후위 탐색한 결과를 출력하는 문제입니다.

파이썬에는 딕셔너리라는 편리한 자료형이 있어 노드의 자식을 편리하고 간단하게 표현할 수 있습니다. 트리의 루트는 A로 고정이므로 전위 탐색, 중위 탐색, 후위 탐색하는 각각의 함수를 구현하고 첫 노드로 루트 노드인 A를 넣어줌으로써 구현할 수 있습니다. 탐색 알고리즘 구현 방법은 재귀(Recursion)을 사용하여 자식이 존재하는 경우에만 탐색하도록 하고 조건에  맞춰 노드를 출력하도록 구현했습니다.

트리를 재귀를 사용해서 탐색하는 방법만 알면 간단히 구현할 수 있는 문제였습니다.