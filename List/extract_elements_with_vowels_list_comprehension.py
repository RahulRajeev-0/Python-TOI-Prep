'''
question -> create a new list using list comprehension this list should include 
string that starts with vowels 
'''

words = ['rahul', 'rajeev', 'abhijith', 'ajith', 'elen']
newList = [word for word in words if word[0] in {'a','e','i','o','u'}]
print(newList)