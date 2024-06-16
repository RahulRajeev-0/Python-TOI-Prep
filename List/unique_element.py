"""
question -> find the non repeating element in list 
(unique)
"""

my_list2 = [3, 1, 2, 3, 1, 2, 4, 5,6,7,99,999,9,9,0,9]


l = [i for i in my_list2 if my_list2.count(i) == 1]
print(l)