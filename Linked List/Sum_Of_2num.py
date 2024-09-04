class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def addTwoNumbers(self, l1, l2):
        dummy = Node(0)
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0

            sum = dig1 + dig2 + carry
            dig = sum % 10
            carry = sum // 10

            new = Node(dig)
            head.next = new
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummy.next
        return result

    def print(self, head):
        if head is None:
            print("Linked List is Empty")
            return

        ptr = head
        while ptr:
             print(ptr.val, end=" ")
             ptr = ptr.next  
        print()      

if __name__ == "__main__":
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)
    #num1 = 342 => ll = 2->4->3

    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)
    #num2 = 465 => ll = 5->6->4

    ll = LinkedList()
    result = ll.addTwoNumbers(l1, l2)     # result = 807 => 7->0->8
    ll.print(result)
