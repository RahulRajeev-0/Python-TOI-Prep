'''
Given a singly linked list , reverse the given linked list
'''

def revser(linked_list):
    if not linked_list.head: return 
    prev = None
    curr = linked_list.head
    while curr :
        _next = curr.next
        curr.next = prev
        prev = curr
        curr = _next
    linked_list.head = prev