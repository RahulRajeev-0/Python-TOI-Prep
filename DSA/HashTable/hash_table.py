'''
This is the basic implementation of hash table without using any collision handling methods
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
    
    # a simple hash function to generate hash code 
    def hash_function(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.size # returning hash code 

    def add(self, key, value):
        hash_code = self.hash_function(key)
        self.array[hash_code] = value
        return 
    
    def get(self, key):
        hash_code = self.hash_function(key)
        return self.array[hash_code]
    
    
hash_map = HashTable(10)
hash_map.add("rahul", 10)
print(hash_map.get('rahul'))
print(hash_map.get('hello'))

    

