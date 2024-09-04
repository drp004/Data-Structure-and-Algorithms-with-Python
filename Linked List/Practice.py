class Node:
    
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

class Linkedlist:

    def __init__(self):
        self.head = None

    def insert_at_beging(self, data):
        node = Node(data, self.head)
        self.head = node 

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = Node(data, None) 

    def insert_at_anyposition(self, data, index):
        if index < 0 or index >= self.getlength():
            print("Invalid Index")
            return

        if index == 0:
            self.insert_at_beging(data)
            return    

        count = 0
        ptr = self.head
        while ptr:
            if count == index - 1 :
                node = Node(data, ptr.next)
                ptr.next = node
            count += 1    
            ptr = ptr.next

    def getlength(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next

        return count 


    def remove_from_beging(self):
        self.head = self.head.next
        return    

    def remove_from_end(self):
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None
        return 

    def remove_at(self, index):
        if index < 0 or index >= self.getlength() :
            print("Invalid Index")
            return

        if index == 0:
            self.remove_from_beging()

        ptr = self.head
        count = 0
        while ptr:
            if count == index - 1 :
                ptr.next = ptr.next.next
            count += 1
            ptr = ptr.next
        return    

    def replace_at(self, data, index) :
        if index < 0 or index >= self.getlength() :
            print("Invalid Index")
            return

        if index == 0:
            self.head.data = data
            return

        ptr = self.head
        count = 0
        while ptr:
            if count == index :
                ptr.data = data
            count += 1
            ptr = ptr.next
        return                

    def print(self):
        if self.head is None:
            print("LinkeList is Empty")
            return

        ptr = self.head
        while ptr:
            print(ptr.data, end = " ")
            ptr = ptr.next
        print()    

 
if __name__ == "__main__" :
    ll = Linkedlist()
    ll.insert_at_beging(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(5)
    ll.insert_at_anyposition(4, 3)
    ll.print()
    ll.replace_at(3, 3)
    ll.print()
    ll.remove_from_beging()
    ll.remove_at(2)
    ll.remove_from_end()
    ll.print()