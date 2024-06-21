'''
question -> find the total number of paliyandrom present in the given word

input = 'malayalam'
output = 6

1)malayalam 
2)alayala
3)layal
4)aya
5)ala
6)ala
'''

def find_count_of_paliyandrom(s:str)  -> str:
    count = 0
    for i in range(len(s)):
        for j in range(i + 2,len(s)+1):
            tem = s[i:j]
            if tem == tem[::-1]:
                count += 1
    return count

s = 'malayalam'
print(find_count_of_paliyandrom(s))