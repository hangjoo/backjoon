caseNum = int(input())

for _ in range(caseNum):
    repeatNum, strLine = list(input().split())
    for idx in range(len(strLine)):
        print(strLine[idx] * int(repeatNum), end="")
    print()
