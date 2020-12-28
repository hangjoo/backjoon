import sys


class Deck:
    def __init__(self):
        self.elements = []

    def push_front(self, x):
        self.elements.insert(0, x)

    def push_back(self, x):
        self.elements.append(x)

    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.elements.pop(0)

    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.elements.pop(-1)

    def size(self):
        return len(self.elements)

    def empty(self):
        if self.elements:
            return 0
        else:
            return 1

    def front(self):
        if self.empty():
            return -1
        else:
            return self.elements[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.elements[-1]


n = int(sys.stdin.readline())
deque = Deck()
for _ in range(n):
    inst = sys.stdin.readline().split()
    if inst[0] == "push_front":
        deque.push_front(inst[1])
    elif inst[0] == "push_back":
        deque.push_back(inst[1])
    elif inst[0] == "pop_front":
        sys.stdout.write(str(deque.pop_front()))
        sys.stdout.write("\n")
    elif inst[0] == "pop_back":
        sys.stdout.write(str(deque.pop_back()))
        sys.stdout.write("\n")
    elif inst[0] == "size":
        sys.stdout.write(str(deque.size()))
        sys.stdout.write("\n")
    elif inst[0] == "empty":
        sys.stdout.write(str(deque.empty()))
        sys.stdout.write("\n")
    elif inst[0] == "front":
        sys.stdout.write(str(deque.front()))
        sys.stdout.write("\n")
    elif inst[0] == "back":
        sys.stdout.write(str(deque.back()))
        sys.stdout.write("\n")
