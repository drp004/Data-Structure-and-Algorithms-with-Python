from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        return self.queue.pop()

    def show(self):
        print("Queue is :", end=" ")
        for i in self.queue:
            print(i, end=" ")

    def peek(self):
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)       


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.show()) 
    print("Popped Element is: ", q.dequeue())
    print(q.show()) 