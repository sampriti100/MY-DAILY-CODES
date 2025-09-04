#implementing a single linked list : 
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

    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

   
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    
    def delete(self, key):
        temp = self.head

       
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        
        if not temp:
            print(f"Node with data {key} not found.")
            return

       
        prev.next = temp.next
        temp = None

    
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


# Example usage:
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.print_list()

ll.prepend(5)
ll.print_list()  

ll.delete(20)
ll.print_list()  

print(f"Length of the list: {ll.length()}") 

print(f"Is 10 in the list? {ll.search(10)}")  
print(f"Is 20 in the list? {ll.search(20)}")  
