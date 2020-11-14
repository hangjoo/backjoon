wordNum = int(input())
lenDict = {num: [] for num in range(1, 51)}
for idx in range(wordNum):
    word = input()
    if word not in lenDict[len(word)]:
        lenDict[len(word)].append(word)

for item in lenDict.values():
    if len(item) != 0:
        item.sort()
        for idx in item:
            print(idx)
