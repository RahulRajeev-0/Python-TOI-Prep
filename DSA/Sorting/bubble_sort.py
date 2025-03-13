'''
Bubble sort is a simple sorting algorithm that repeatedly 
compares adjacent elements and swaps them if they are in 
the wrong order. The algorithm iterates through the list multiple times, 
with each pass comparing adjacent pairs of elements and swapping them if necessary. 
This process "bubbles" the largest (or smallest) element to the end of the list. 
After each iteration, the largest (or smallest) element is in its correct position. 
The algorithm continues until the entire list is sorted. 
Bubble sort has a time complexity of O(n^2), where n is the number of elements in the list.

Imp* => Stable sorting algorithm  

Advantages:
1. Easy to understand and implement.
2. Requires minimal additional space, as it operates in-place.

Disadvantages:
1. Inefficient for large datasets, as it has a time complexity of O(n^2).
2. Not suitable for nearly sorted or reverse-ordered data, as it requires multiple passes to sort elements.

'''
# bubble sort

def bubble_sort(nums: list) -> list:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

l = [3,66,1,77,8,9]
print(bubble_sort(l))

