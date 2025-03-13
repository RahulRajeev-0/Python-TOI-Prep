
'''
Quick sort is a popular sorting algorithm that uses a divide-and-conquer 
approach to efficiently sort a list of elements. It works by selecting a 
"pivot" element from the list and partitioning the other elements into two 
sublists, according to whether they are less than or greater than the pivot. 
The pivot is then placed in its correct sorted position, with all elements smaller 
than the pivot appearing before it, and all elements larger than the pivot appearing 
after it. This process is recursively applied to the sublists on either side of the 
pivot until the entire list is sorted. Quick sort is known for its average-case 
time complexity of O(n log n), making it one of the fastest sorting algorithms in practice.
However, in the worst case, it can have a time complexity of O(n^2) if the pivot selection is unbalanced.

'''
def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [num for num in nums[1:] if num < pivot]
    right = [num for num in nums[1:] if num >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

l = [3,66,1,77,8,9]

print(quick_sort(l))
