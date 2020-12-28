n = int(input())
n_list = list(map(int, input().split()))
n_dict = {}
for i in n_list:
    if i in n_dict.keys():
        n_dict[i] += 1
    else:
        n_dict[i] = 1

m = int(input())
m_list = list(map(int, input().split()))
for i in m_list:
    if i in n_dict.keys():
        print(n_dict[i], end=" ")
    else:
        print(0, end=" ")
