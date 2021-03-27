import re


def solution(new_id: str):
    # step 1
    new_id = new_id.lower()
    print(new_id)

    # step 2
    white_list = [chr(ord("a") + i) for i in range(26)] + [str(i) for i in range(10)] + ["-", "_", "."]
    for char in new_id:
        if char not in white_list:
            new_id = new_id.replace(char, "")
    new_id = re.sub("^[a-zA-Z0-9-_.]", "", new_id)
    print(new_id)

    # step 3
    new_id = re.sub(".{2,}", ".", new_id)
    print(new_id)

    # step 4
    new_id = new_id.strip(".")
    print(new_id)

    # step 5
    if not new_id:
        new_id = "a"
    print(new_id)

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip(".")
    print(new_id)

    while len(new_id) <= 2:
        new_id += new_id[-1]
    print(new_id)

    answer = new_id
    return answer
