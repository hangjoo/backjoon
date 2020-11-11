T = int(input())

for _ in range(T):
    str = input()
    stack = 0
    for i in range(len(str)):
        if str[i] == '(':
            stack += 1
        elif str[i] == ')':
            stack -= 1

        if stack < 0:
            break

    if stack == 0:
        print("YES")
    else:
        print("NO")