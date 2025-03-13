'''
Find the middle element in linked list 

common question and other questions like delete the middle element

'''

def middle_ele(linked_list):
    if not linked_list.head:
        print("The linked list is empty")
        return
    slow = fast = linked_list.head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    print("middle element = ", slow.val)


    

