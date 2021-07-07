n = int(input())

prev_none = 1
prev_left = 1
prev_right = 1

for i in range(1, n):
    fill_none = prev_none + prev_left + prev_right
    fill_left = prev_right + prev_none
    fill_right = prev_left + prev_none

    prev_none = fill_none
    prev_left = fill_left
    prev_right = fill_right

print(sum([prev_none, prev_left, prev_right]) % 9901)
