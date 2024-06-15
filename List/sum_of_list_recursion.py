'''
question -> write a recursive function to find sum of all elements in a list 
'''

l = [16,4,22,3,4,1,9,0]

def sum_of_array(arr: list) -> int :
    # base case
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_of_array(arr[1:])

print(sum_of_array(l))