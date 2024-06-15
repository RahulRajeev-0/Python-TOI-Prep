'''
question -> find the count of capital and small letter in the string 

'''

s = "RahuLRAJeev"

def is_capital(char):
    ascii_val = ord(char)
    if 65 <= ascii_val <= 90:
        return True
    else:
        return False
    
def is_small(char):
    ascii_val = ord(char)
    if 97 <= ascii_val <= 122:  # ASCII values for 'a' to 'z'
        return True
    else:
        return False

def count_small_upper(s):
    count_capital, count_small = 0, 0
    for i in s:
        if is_capital(i):
            count_capital += 1
        elif is_small(i):
            count_small += 1
    return {'capital':count_capital, 'small':count_small}

print(count_small_upper(s))