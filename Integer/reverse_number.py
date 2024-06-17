'''
question -> reverse the given number without converting to string 

'''

def reverse_number(number):
    temp = number
    res = 0
    while temp > 0:
        last = temp % 10
        res = res * 10 + last
        temp //= 10
    return res

print(reverse_number(1234))