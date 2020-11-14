ascending = [num for num in range(1, 9)]
descending = [num for num in range(8, 0, -1)]

music = list(map(int, input().split()))
if music == ascending:
    print("ascending")
elif music == descending:
    print("descending")
else:
    print("mixed")