def binarySearch(list: list, target: int, front: int, end: int):
    # return index, whether taget exists
    while front < end:
        pivot = int((front + end) / 2)
        if target == list[pivot]:
            return pivot, True
        elif target < list[pivot]:
            end = pivot - 1
        else:
            front = pivot + 1
    return front, True if target == list[front] else False


numCount = int(input())
numList = list(map(int, input().split()))
orderedList = []
for num in numList:
    if len(orderedList) == 0:
        orderedList.append(num)
    else:
        idx, ret = binarySearch(orderedList, num, 0, len(orderedList) - 1)
        if not ret:
            # num doesn't eixst in orderedList.
            if num < orderedList[idx]:
                orderedList.insert(idx, num)
            elif num > orderedList[idx]:
                orderedList.insert(idx + 1, num)
            else:
                pass

tgtCount = int(input())
tgtList = list(map(int, input().split()))
for tgt in tgtList:
    _, ret = binarySearch(orderedList, tgt, 0, len(orderedList) - 1)
    if ret:
        print(1)
    else:
        print(0)