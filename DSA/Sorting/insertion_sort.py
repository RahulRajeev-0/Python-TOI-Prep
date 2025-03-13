'''
Insertion sort is a simple sorting algorithm that iteratively builds a 
sorted sublist by inserting elements into their correct positions within 
the sublist. It is an in-place sorting algorithm, meaning it sorts the 
elements within the original list without requiring additional memory.

The insertion sort algorithm has a time complexity of O(n^2) in the worst case 
and average case, where n is the number of elements in the list. It performs well
on small lists or partially sorted lists but can be inefficient for large lists 
compared to more advanced sorting algorithms like merge sort or quicksort.


sort algorithm:

1. Start with the second element in the list. Assume that the first element 
is already sorted.

2. Compare the second element with the first element. If the second element 
is smaller, swap them so that the smaller element is in the first position.

3. Move to the next element (third element) and compare it with the elements 
in the sorted sublist (first and second elements). Insert the element into 
its correct position within the sorted sublist by shifting the larger elements to the right.

4. Repeat step 3 for each subsequent element in the list, inserting it into 
the appropriate position within the sorted sublist.

5. Continue this process until all elements in the list are sorted.


Advantages:
1. Simple and easy to implement.
2. Efficient for small datasets or partially sorted data.
3. Performs well with data that is already mostly sorted.

Disadvantages:
1. Inefficient for large datasets, as it has a time complexity of O(n^2).
2. As it compares and shifts elements one by one, it can be slow for large 
datasets with significant disorder.

'''
# insertion sort 


l = [3,66,1,77,8,9]

def insertion_sort_while_loop(l: list) -> list:
    # assumes the first element as aready sorted 
    low = 1
    high = len(l) - 1
    while low <= high:
        key = l[low]
        prev = low - 1

        while prev >= 0 and l[prev] > key:
            l[prev + 1] = l[prev]
            prev -= 1
        
        l[prev + 1] = key
        low += 1
    return l


print(insertion_sort_while_loop(l))


def insertion_sort_for_loop(l: list) -> list:
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = key
            j -= 1
        l[j + 1] = key
        
    return l


print(insertion_sort_for_loop(l))
