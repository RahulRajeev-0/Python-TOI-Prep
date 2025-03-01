nested_list = [1, [2, [3, 4], 5], [6, 7], 8, [9, [10, 11]]]

def get_depth(arr):
    if isinstance(arr, list):
        max_depth = 0
        for item in arr:
            item_depth = get_depth(item)
            if item_depth > max_depth :
                max_depth = item_depth
        return 1 + max_depth
    else : return 0

print(get_depth(nested_list))



