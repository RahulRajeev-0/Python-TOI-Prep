'''
question -> Reverse nested list 

l = [1,2,[3,4],[6,[7,8]]]

output = [[[8,7],6],[3,4],2,1]


'''

# recursive function 

l = [1,2,[3,4],[6,[7,8]]]

def reverse_nested_array(arr: list) -> list: 
    res = []
    for value in arr[::-1]:
        if isinstance(value, list):
            res.append(reverse_nested_array(value))
        else:
            res.append(value)
    return res

print(reverse_nested_array(l))

def ress(str1):
    return [ress(i) if isinstance(i,list) else i for i in str1[::-1]]

print(ress(l))