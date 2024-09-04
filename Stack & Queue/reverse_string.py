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
        print("Reverse String is :")
        while i>=0:
            print(self.stack[i], end="")
            i -= 1

    def reverse_str(self, string):
        size = len(string)
        for i in range(size):
            self.push(string[i])

        self.show()    

if __name__ == "__main__":
    s = Stack()
    string = "I am Dhruv"
    print("String is :\n", string)
    s.reverse_str(string)