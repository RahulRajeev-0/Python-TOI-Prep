'''
question = > Create a list and delete duplicate without using another list 
'''

# method 1 (sometimes not accepted by the reviewer)

l = [1,1,1,1,1,2,3,4,]

l = list(set(l))
print(l)


# method 2

def remove_duplicate(arr: list) :
    seen = set()
    i = len(arr) - 1

    while i >= 0:
        if arr[i] != seen:
            seen.add(arr[i])
        else:
            del arr[i]
        i -= 1

remove_duplicate(l)
print(l)




