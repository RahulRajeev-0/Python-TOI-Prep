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


# without using set , another list and dict 

# method 1 sort the array 

def remove_duplicate_sort(arr: list):
    arr.sort()
    i = 1
    while i < len(arr):
        if arr[i -1] == arr[i]:
            del arr[i]
        else:
            i += 1


my_list = [3, 1, 2, 3, 1, 2, 4, 5]
remove_duplicate_sort(my_list)
print(my_list)

#  method 2 in place 

def remove_duplicates_in_place(lst):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[j] == lst[i]:
                del lst[j]  # Remove the duplicate
            else:
                j += 1
        i += 1

 
my_list2 = [3, 1, 2, 3, 1, 2, 4, 5,6,7,99,999,9,9,0,9]

remove_duplicates_in_place(my_list2)
print(my_list2)







