from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def show(self):
        i = len(self.stack)-1
        print("Stack is :")
        while i>=0:
            print(self.stack[i])
            i -= 1

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.show()
    print("Popped element is :", s.pop())
    s.show()                
