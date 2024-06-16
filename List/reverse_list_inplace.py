'''
question -> reverse a list in place
'''

# method 1 using in build function 

l = [1,2,3,4,6]
l.reverse()
print(l)

# method 2 usingn slicing 
l = l[::-1]
print(l)


# method 3 using two pointer 


    
def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print(my_list)