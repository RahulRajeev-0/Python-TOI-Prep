'''
question ) 

create a string with multiple words with spaces, all in lower case . 
convert the first and last char to uppercase
'''

s = 'my name is rahul Rajeev'


# method 1

def convert_to_first_and_last_upper(s:str):
    words = s.split()
    modified_words = []

    for word in words:
        if len(word) > 1:
            modified_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            modified_word = word.uper()
        modified_words.append(modified_word)
    return " ".join(modified_words)



print(convert_to_first_and_last_upper(s))



# method 2  (without using upper function and using ASCII value ) 
# ASCII value of CAPITAL letter is less than the SMALL Letters
# Capital = 65(A) - 90(Z)
#  Small = 97(a) - 122(z)




def capitalize_first(s:str):

    # helper function - to change smallercase to uppercase 
    def to_upper(char):
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            return char(ascii_val - 32)
        return char
    
    words = s.split()
    modified_words = []

    for word in words:
        if len(word) > 1:
            modified_word = to_upper(word[0]) + word[1 : -1] + to_upper(word[-1])
        else:
            modified_word = to_upper(word)
        modified_words.append(modified_word)
    return " ".join(modified_words)









