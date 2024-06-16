'''
question -> combine two sorted array in O(n) or less time 

'''

# use merge sorts merge function to do this in O(n)

def merge(left, right):
    left_index = 0
    right_index = 0
    len_left = len(left) 
    len_right = len(right)
    merged_array = []

    while left_index < len_left and right_index < len_right:
        if left[left_index] < right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    while len_left > left_index:
        merged_array.append(left[left_index])
        left_index += 1


    while len_right > right_index:
        merged_array.append(right[right_index])
        right_index += 1

    return merged_array



arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

result = merge(arr1, arr2)
print(result)