while True:
    numStr = input()
    if numStr == "0":
        break
    else:
        flag = True
        for idx in range(int(len(numStr) / 2) + 1):
            if numStr[idx] != numStr[-idx - 1]:
                flag = False
                break
        if flag:
            print("yes")
        else:
            print("no")