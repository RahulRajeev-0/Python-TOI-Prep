'''
question -> swap the first and last digit of a number without using string 
'''

def swap_first_and_last_digit(number: int):
    if number < 10:
        return number

    length_of_number = 0
    tem = number
    while tem:
        length_of_number += 1
        tem //= 10
#     first number
    first = number // (10 ** (length_of_number - 1))
    print(first)
# last number
    last = number % 10
    print(last)
# middle number
    middle = number % (10 ** (length_of_number - 1))
    middle = middle // 10

    return last * 10 ** (length_of_number -1 ) + middle * 10 + first


print(swap_first_and_last_digit(1234))