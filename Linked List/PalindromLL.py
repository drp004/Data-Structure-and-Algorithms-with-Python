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
        return    

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next
    
        ptr.next = Node(data, None)

    def insert_at_anyposition(self, data, index):
        if self.head is None or index == 0:
            insert_at_beging(data)
            return

        ptr = self.head
        i = 0
        while i < index:
            i += 1
            ptr = ptr.next

        ptr.next = Node(deta, ptr.next)
        return

    def getlength(self):
        count = 0
        ptr = self.head
        while ptr.next:
            count += 1
            ptr = ptr.next
        return count 

    def reverseLL(self, head):
        if head is None or head.next is None:
            return head  

        new = self.reverseLL(head.next)
        head.next.next = head
        head.next = None

        return new 

    def isLLpalindrome(self):
        if self.head is None or self.head.next is None:
            return True

        ptr = self.head
        size = self.getlength()
        i = 0
        while i < (size//2)+1 :
            i += 1
            ptr = ptr.next
            
        mid = ptr
        ptr2 = self.reverseLL(mid)
        ptr = self.head
        #print(ptr.next.data)

        while ptr and ptr2 :
            if ptr.data != ptr2.data :
                return False
            ptr = ptr.next
            ptr2 = ptr2.next
        return True

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        ptr = self.head
        while ptr:
             print(ptr.data, end=" ")
             ptr = ptr.next  
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_beging(2)
    ll.insert_at_beging(2)
    ll.insert_at_beging(1)
    ll.print()
    print(ll.isLLpalindrome())
