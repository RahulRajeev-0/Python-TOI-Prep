'''
question -> flate a nested list 


'''

# recursion

def flatten_list(nested_list: list) -> list :
    flat_list = []

    def flatten(element):
        if isinstance(element, list):
            for item in element:
                flatten(item)
        else:
            flat_list.append(element)
    flatten(nested_list)
    return flat_list

nested_list = [1, [2, [3, 4], 5], [6, 7], 8, [9, [10, 11]]]


print(flatten_list(nested_list))
