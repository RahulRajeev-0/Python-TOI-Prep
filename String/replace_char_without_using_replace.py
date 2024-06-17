'''
question -> replace the char in given string without using in build string function replace 

'''

s = 'rhaul'


def replace_char(word:str, old_character : str, new_character: str) -> str:
    l = list(word)

    for i in range(len(l)):
        if l[i] == old_character:
            l[i] = new_character
    word = "".join(l)
    return word

s = replace_char(s,'r','R')
print(s)
