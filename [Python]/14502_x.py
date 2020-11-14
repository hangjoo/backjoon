row, col = list(map(int, input().split()))

mapArr = []
emptyArr = []
virusArr = []

for _ in range(row):
    colArr = list(map(int, input().split()))
    mapArr.append(colArr)
for i in range(row):
    for j in range(col):
        if mapArr[i][j] == 0:
            emptyArr.append((i, j))
        elif mapArr[i][j] == 2:
            virusArr.append((i, j))
safeCount = 0
for pos_i in range(len(emptyArr) - 2):
    for pos_j in range(pos_i + 1, len(emptyArr) - 1):
        for pos_k in range(pos_j + 1, len(emptyArr)):
            runEmpty = emptyArr.copy()
            runVirus = virusArr.copy()
            runEmpty.remove((emptyArr[pos_i][0], emptyArr[pos_i][1]))
            runEmpty.remove((emptyArr[pos_j][0], emptyArr[pos_j][1]))
            runEmpty.remove((emptyArr[pos_k][0], emptyArr[pos_k][1]))

            while len(runVirus) != 0:
                virus = runVirus.pop(0)
                for i in range(-1, 2, 2):
                    if virus[0] + i in list(range(0, row)) and (virus[0] + i, virus[1]) in runEmpty:
                        runEmpty.remove((virus[0] + i, virus[1]))
                        runVirus.append((virus[0] + i, virus[1]))
                    if virus[1] + i in list(range(0, col)) and (virus[0], virus[1] + i) in runEmpty:
                        runEmpty.remove((virus[0], virus[1] + i))
                        runVirus.append((virus[0], virus[1] + i))

            if safeCount < len(runEmpty):
                safeCount = len(runEmpty)

print(safeCount)
