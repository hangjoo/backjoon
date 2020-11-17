numCount = int(input())
numList = [num for num in range(1, numCount + 1)]

abandon = True
curList = numList.copy()
while len(curList) > 1:
    tempList = []
    for idx in range(len(curList)):
        if abandon:
            pass
        else:
            tempList.append(curList[idx])
        abandon = not abandon
    curList = tempList.copy()

print(curList[0])