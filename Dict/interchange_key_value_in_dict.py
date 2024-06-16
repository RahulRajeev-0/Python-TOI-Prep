'''
question -> given a dictionary , interchange the key => as values and values as => keys 

'''


dictionary = {'name':'rahul', 'father':'rajeev'}

def interchange_key_value(d: dict)-> dict:
    
    for i in list(d.keys()): # ---> ['name', 'father']
        d[d.pop(i)] = i           
    return d
print(interchange_key_value(dictionary))   