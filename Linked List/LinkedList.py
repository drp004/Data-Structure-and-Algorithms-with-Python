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
            node = Node(data, None)
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

    def remove_at(self, index):
        if index < 0 or index >= self.getlength():
            print("Invalid Index")
            return
        
        ptr = self.head
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        while ptr.next:
            if count == index -1 :
                ptr.next = ptr.next.next
            ptr = ptr.next 
            count += 1      
        return

    def remove_at_beging(self):
        self.head = self.head.next
        return    

    def remove_at_end(self):
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None  
        return 

    def replace_at(self, data, index):
        if index < 0 or index >= self.getlength():
            print("Invalid Index")
            return
        
        ptr = self.head
        if index == 0:
            self.head.data = data
            return

        count = 0
        while ptr.next:
            if count == index :
                ptr.data = data
            ptr = ptr.next 
            count += 1      
        return     

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        ptr = self.head
        while ptr:
             print(ptr.data, end=" ")
             ptr = ptr.next  
        print()  
                       
    def nthnode(self, num):
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        i = 1
        ptr = self.head
        while i < count - num :
            ptr = ptr.next
            i += 1
        ptr.next = ptr.next.next
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beging(5)
    ll.insert_at_beging(4)
    ll.insert_at_beging(3)
    ll.insert_at_beging(2)
    ll.insert_at_beging(1) 
    ll.insert_at_end(6) 
    ll.insert_at_anyposition(0, 0)
    ll.print()
    ll.nthnode(3)
    ll.print()
    '''ll.reverse()
    ll.print()
    print(ll.getlength())
    ll.remove_at_end()
    ll.remove_at(10)
    ll.remove_at_beging()
    ll.replace_at(2,2)
    ll.print()'''          