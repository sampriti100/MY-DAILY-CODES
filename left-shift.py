#given a singly linked list of size N . the task is to left-shift the linked list by k nodes , where k is a given positiive integer smaller than or equal to length of linked list .
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Utility function to append node to the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    # Function to perform left shift by k nodes
    def left_shift(self, k):
        if self.head is None or k == 0:
            return
        
        # Find the length of the linked list
        length = 1
        current = self.head
        while current.next:
            length += 1
            current = current.next
        
        # If k is greater than or equal to length, use k = k % length
        k = k % length
        if k == 0:
            return
        
        # Find the k-th node
        current = self.head
        for _ in range(k - 1):
            current = current.next
        
        # current is now at the k-th node
        kth_node = current
        
        # Find the last node
        last_node = kth_node
        while last_node.next:
            last_node = last_node.next
        
        # Change the head to the node right after the k-th node
        new_head = kth_node.next
        # Set the k-th node's next to None
        kth_node.next = None
        # Connect the last node's next to the previous head
        last_node.next = self.head
        # Update the head of the list
        self.head = new_head

    # Utility function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Test the function
if __name__ == "__main__":
    ll = LinkedList()
    
    # Append some data to the list
    for i in range(1, 6):
        ll.append(i)

    print("Original List:")
    ll.print_list()

    # Perform left shift by k nodes
    k = 2
    ll.left_shift(k)

    print(f"List after left shift by {k} nodes:")
    ll.print_list()
