'''
question -> write a function to merge two linked list 


'''

def merge_linked_list(left, right):
    if left.head is None:
        return right
    if right.head is None:
        return left
    
    node = left.head
    while node.next:
        node= node.next
    node.next = right.head

    return left.head


