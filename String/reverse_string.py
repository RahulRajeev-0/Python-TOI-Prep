'''
question -> reverse string

since there are many method to reverse a string 
we will look into some not every method
'''

s = 'hello'

# slicing
def reverse_string(s:str) -> str :
    return s[::-1]

# recursion
def reverse_using_recursion(s: str) -> str:
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

# using loop 
def reverse_using_loop(s: str) -> str:
    res = ""
    for i in range(len(s) -1, -1, -1):
        res += s[i]
    return res

# another loop method 
def reverse_using_loop2(s):
    res = ""
    for i in s:
        res = i + res
    return res

print(reverse_using_loop2(s))
