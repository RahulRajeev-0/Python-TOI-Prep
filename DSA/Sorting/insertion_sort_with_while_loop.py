'''
question -> insertion sort using only while loop

'''


l = [3,66,1,77,8,9]

def insertion_sort(l: list) -> list:
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

print(insertion_sort(l))
