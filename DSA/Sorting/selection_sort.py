'''
Selection sort is a simple sorting algorithm that works by repeatedly 
finding the minimum (or maximum) element from an unsorted portion of 
the list and placing it at the beginning of the sorted portion. 
The algorithm divides the list into two parts: the sorted portion at 
the beginning and the unsorted portion at the end. In each iteration, 
the smallest (or largest) element from the unsorted portion is selected 
and swapped with the first element of the unsorted portion. This process
continues until the entire list is sorted. Selection sort has a time 
complexity of O(n^2), where n is the number of elements in the list.

'''

def selection_sort(nums: list) -> list:
    for i in range(len(nums)):
        min_ele = min(nums[i:])
        index_min_ele = nums.index(min_ele)
        if nums[i] != min_ele:
            nums[i], nums[index_min_ele] =  nums[index_min_ele], nums[i]
    return nums

l = [3,66,1,77,8,9]
print(selection_sort(l))

