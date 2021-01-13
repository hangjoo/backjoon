import sys

m = int(sys.stdin.readline())
ALL_ON = 1048575
ALL_OFF = 0
bit = 0
for _ in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "add":
        bit |= 1 << (int(cmd[1]) - 1)
    elif cmd[0] == "remove":
        bit = bit & (ALL_ON ^ (1 << (int(cmd[1]) - 1)))
    elif cmd[0] == "check":
        if (bit >> (int(cmd[1]) - 1)) & 1 == 1:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif cmd[0] == "toggle":
        bit ^= 1 << (int(cmd[1]) - 1)
    elif cmd[0] == "all":
        bit = ALL_ON
    elif cmd[0] == "empty":
        bit = ALL_OFF
