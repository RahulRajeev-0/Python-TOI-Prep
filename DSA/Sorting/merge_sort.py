'''
Merge sort is a popular sorting algorithm that follows the divide-and-conquer paradigm.
It efficiently sorts a list of elements by repeatedly dividing it into smaller sublists, 
sorting them individually, and then merging them back together.

Here's a step-by-step explanation of the merge sort algorithm:

1. Divide: The input list is recursively divided into two halves 
until the sublists contain only one element or are empty.

2. Conquer: Once the sublists reach their base case (single element or empty), 
they are considered sorted.

3. Merge: The sorted sublists are merged back together by comparing the 
elements in pairs and placing them in the correct order. This process is 
repeated until a single sorted list is obtained.

The merge sort algorithm has a time complexity of O(n log n) in all cases. 
It offers stable sorting (preserves the relative order of equal elements) and 
is well-suited for sorting large lists or when stability is required. However, 
merge sort has a space complexity of O(n) due to the additional space required 
for merging the sublists.

'''

# merge is the helper function to create sorted array from the divided array
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1 
    
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    return merge(left_arr, right_arr)


l = [3,66,1,77,8,9]

print(merge_sort(l))