def check(string):
    vowel_count = 0
    for alphabet in string:
        if alphabet in vowels:
            vowel_count += 1
    if vowel_count >= 1 and len(string) - vowel_count >= 2:
        return True
    else:
        return False


def find(ret, cand):
    global l
    if len(ret) == l and check(ret):
        print(ret)
    elif len(cand) == 0:
        pass
    else:
        for i in range(len(cand)):
            find(ret + cand[i], cand[i + 1 :])


l, c = map(int, input().split())
alphabets = input().split()
vowels = ["a", "e", "i", "o", "u"]

find("", sorted(alphabets))
