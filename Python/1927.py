import sys


class Heap:
    def __init__(self):
        self.data = [0]

    def add(self, x):
        self.data.append(x)
        self.data[0] += 1
        key = self.data[0]

        while key > 1:
            if self.data[key] < self.data[key // 2]:
                self.data[key], self.data[key // 2] = self.data[key // 2], self.data[key]
                key //= 2
            else:
                break

    def pop(self):
        if self.data[0] == 0:
            return 0
        else:
            self.data[1], self.data[self.data[0]] = self.data[self.data[0]], self.data[1]
            ret = self.data.pop()
            self.data[0] -= 1
            key = 1

            while True:
                next_key = self.check(key)
                if next_key != -1:
                    if self.data[key] > self.data[next_key]:
                        self.data[key], self.data[next_key] = self.data[next_key], self.data[key]
                        key = next_key
                    else:
                        break
                else:
                    break

            return ret

    def check(self, key):
        left, right = _, _

        if key * 2 <= self.data[0]:
            left = self.data[key * 2]
        else:
            left = float("inf")

        if key * 2 + 1 <= self.data[0]:
            right = self.data[key * 2 + 1]
        else:
            right = float("inf")

        if left == right == float("inf"):
            return -1
        elif left <= right:
            return key * 2
        else:
            return key * 2 + 1

    def __str__(self):
        return str(self.data)


n = int(sys.stdin.readline()[:-1])
heap = Heap()

for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        sys.stdout.write(str(heap.pop()))
    else:
        heap.add(cmd)
