'''
question -> create a singly linked list 
'''

class Node:
    def __init__(self, data = None):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # function for adding new node 
    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(data)
    
    # function for printing all the data(val) in linked list
    def print_all(self):
        if self.head :
            node = self.head
            while node != None:
                print(node.val)
                node = node.next
        else:
            print("there is no data")

    # function for removing a node from linked list
    def remove(self, val):
        # Case 1: If there is no data (empty list)
        if not self.head:
            print("The linked list is empty.")
            return

        # Case 2: If the node to be deleted is the head node
        if self.head.val == val:
            self.head = self.head.next  # Move the head pointer to the next node
            print(f"{val} data removed from linked list")
            return

        # Case 3: If the node to be deleted is somewhere in the middle or end
        node = self.head
        while node.next:
            if node.next.val == val:  # Check if the next node contains the value
                node.next = node.next.next  # Skip the node to delete it
                print(f"{val} data removed from linked list")
                return
            node = node.next  # Move to the next node

        # If the value was not found
        print(f"The given value {val} is not found in the linked list.")




    
    

            


