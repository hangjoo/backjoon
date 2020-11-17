def quickSort(numList: list, front: int, end: int):
    if front < end:
        idx = front
        pivot = end
        while idx < pivot:
            if numList[idx] > numList[pivot]:
                numList.insert(pivot + 1, numList[idx])
                numList.pop(idx)
                pivot -= 1
            else:
                idx += 1
        quickSort(numList, front, pivot - 1)
        quickSort(numList, pivot + 1, end)


numList = []
numCount = int(input())
for _ in range(numCount):
    num = int(input())
    numList.append(num)

# quickSort(numList=numList, front=0, end=len(numList) - 1)
numList.sort()

# print("PRINT START.")
for idx in range(numCount):
    print(numList[idx])
