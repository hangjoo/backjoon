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
