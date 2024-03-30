class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = data
        else: 
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = data

    
    def printer(self):

        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next



    

Node1 = Node("John")
linkedlist = LinkedList()
linkedlist.insert(Node1)
Node2 = Node("Ben")
linkedlist.insert(Node2)
Node3 = Node("Mathew")
linkedlist.insert(Node3)
Node4 = Node("Rushabh")
linkedlist.insert(Node4)

linkedlist.printer()
