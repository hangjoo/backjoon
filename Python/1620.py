import sys

n, m = list(map(int, input().split()))

pokemon_index = {}
pokemon_name = {}
for i in range(1, n + 1):
    name = sys.stdin.readline()[:-1]
    pokemon_index[i] = name
    pokemon_name[name] = i

for _ in range(m):
    ques = sys.stdin.readline()[:-1]
    if ques.isdigit():
        sys.stdout.write(pokemon_index[int(ques)])
        sys.stdout.write("\n")
    else:
        sys.stdout.write(str(pokemon_name[ques]))
        sys.stdout.write("\n")
