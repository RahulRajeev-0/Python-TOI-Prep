'''
questions -> find the longest consecutive subarray from a given array of integers 

'''

def longest_subarray(l: list) -> list:
    res = []
    tem = [l[0]]

    for i in range(1, len(l)):
        if tem[-1] == l[i] - 1 :
            tem.append(l[i])
        else:
            tem = [l[i]]
        
        if len(tem) > len(res):
            res = tem   
    return res

l = [1,2,3,5,6,8,9,10,11,12]
print(longest_subarray(l))
