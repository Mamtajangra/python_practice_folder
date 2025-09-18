class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_linked_list:
    def __init__(self,head = None):
        self.head = head

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("None")







n1 = Node(23)
n2 = Node(33)
n3 = Node(44)
n4 = Node(55)
n5 = Node(66)

head = n1
n1.next = n2
n1.prev = head

n2.next = n3
n2.prev = n1

n3.next = n4
n3.prev = n2

n4.next = n5
n4.prev = n3

n5.prev = n4

DLL= Doubly_linked_list(head)

# DLL.traverse()

DLL.traverse()