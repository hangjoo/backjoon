numCount = int(input())
numStr = input()
numSum = 0
for idx in range(numCount):
    numSum += int(numStr[idx])
print(numSum)