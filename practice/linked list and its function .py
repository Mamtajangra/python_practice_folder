# create a class of node 
class Node:
    # define constructer it shows that node contain data 
    def __init__(self,data):
        # these are the features 
        self.data = data
        self.next = None


# linked list class 
class Linked_list:
    def __init__(self):
        # head is point to none 
        self.head = None




# it is used to print all data in nodes 
    def traverse(self):
        # temporary variable point to head 
        temp = self.head
        # loop and print data of each node 
        while temp:
            print(temp.data,end="-->")
            # move to next node 
            temp = temp.next
        return None



# insert any value at the beginning 
    def insert(self,value):
        new_node = Node(value)
        # again mew node move to the head of another 
        new_node.next = self.head
        # that head become new node 
        self.head = new_node


# append any value at the last of the list 
    def append(self,value):
        new_node = Node(value)
        # case 1 = if list is empty so new node become head 
        if self.head is None:
            self.head = new_node
            return
        # temp point to the head 
        temp = self.head

# case 2 if list is not empty check the elements 
        while temp.next:
            # move to next to next 
            temp = temp.next
            # at last new node attach 
        temp.next = new_node
            # temp = None



# in deletion we have previous node 
    def delete(self,value):
        prev = None
        temp = self.head
# case1 = if list empty
        if temp is None:
            print("no item in list")
            return 
# if data is equal to the value we want to delete 
        if temp.data == value:
            self.head = temp.next
            temp = None
            return

# case3 = if value is not equal to data we move forward 
        while temp and temp.data!=value:
            prev = temp
            temp = temp.next

# list empty 
        if temp is None:
            print("list is empty")
            return 
# find out data lastly 
        prev.next = temp.next  
        temp= None         



# fix value in the node 
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)


# start to link each node 
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# n1 is assign to head 
head = n1
# linked list 


LL1 = Linked_list()
LL1.head = n1
# print actual list 
LL1.traverse()
LL1.insert(100)
LL1.insert(110)
LL1.insert(120)
LL1.insert(130)
LL1.insert(140)
# print after insertion
LL1.traverse()
print("append value")
# append value 
LL1.append(77)

LL1.traverse()
print("after insertion ")
LL1.traverse()
print("delettion")
LL1.delete(120)
LL1.traverse()

