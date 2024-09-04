class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beging(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next
    
        ptr.next = Node(data, None)

    def insert_at_anyposition(self, data, index):
        if index == 0:
            self.insert_at_beging(data)

        if self.head is None:
            node = Node(data, None)
            return

        ptr = self.head
        i=0
        while i<index-1:
            ptr = ptr.next
            i += 1

        node = Node(data, ptr.next)
        ptr.next = node   

    def getlength(self):
        count = 0
        ptr = self.head
        while ptr.next:
            count += 1
            ptr = ptr.next
        return count     

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        ptr = self.head
        while ptr:
             print(ptr.data, end=" ")
             ptr = ptr.next  
        print()   

    def midofLL(self):
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        ptr = self.head
        i = 1
        while i < (count//2)+1:
            ptr = ptr.next    
            i += 1
        return ptr.data

    def mid(self):
        if self.head == None or self.head.next == None:
            return self.head 

        p = self.head
        q = self.head

        while q and q.next:
            p = p.next
            q = q.next.next 

        return p          

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(6)
    ll.insert_at_beging(5)
    ll.insert_at_beging(4)
    ll.insert_at_beging(3)
    ll.insert_at_beging(2)
    ll.insert_at_beging(1) 
    #ll.insert_at_end(6) 
    ll.print()
    mid = ll.midofLL()
    print(mid)
    m = ll.mid()
    print(m.data)