#WAP to covert a string into a linked list of characters - 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def string_to_linked_list(s):
    linked_list = LinkedList()
    for char in s:
        linked_list.append(char)
    return linked_list


string = "sampriti"
linked_list = string_to_linked_list(string)
linked_list.print_list()
