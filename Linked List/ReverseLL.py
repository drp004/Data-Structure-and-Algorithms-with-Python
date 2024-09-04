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

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        ptr = self.head
        while ptr:
             print(ptr.data, end=" ")
             ptr = ptr.next  
        print()   

    def reverse(self):                                     # Using Iteration   1->2->3->4->5
        if self.head==None or self.head.next==None :
            return

        prev = self.head
        curr = self.head.next
        while curr:
            next = curr.next
            curr.next = prev

            # update
            prev = curr
            curr = next  
        self.head.next = None
        self.head = prev 

    def reverseLL(self, head):
        if head is None or head.next is None:
            return head  

        new = self.reverseLL(head.next)
        head.next.next = head
        head.next = None

        return new        

    def mid(self, head):
        p = head
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next

        return p   
     

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beging(5)
    ll.insert_at_beging(4)
    ll.insert_at_beging(3)
    ll.insert_at_beging(2)
    ll.insert_at_beging(1) 
    # ll.insert_at_end(6) 
    ll.print()
    #ll.reverse()
    #ll.print()
    # ll.head = ll.reverseLL(ll.head)
    # ll.print()
    q = ll.mid(ll.head)
    print(q.data)