'''
question -> write the get method of a linear probed hash function 

 note :
this may change depending upon the hash function used for linear probing 
here the hash function will be provided and answer will be related to that
 hash function .
'''

# implementaion of hash table
class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.array = [None for i in range (self.Max)]


    def get_hash(self,key):
        hash_code = 0
        for i in key:
            hash_code += ord(i)
        return hash_code % self.Max
    
    def __setitem__(self, key, value):
        hash_code = self.get_hash(key)
        probe = 0
        while self.array[hash_code] is not None:
            if probe >= self.Max: # for avoiding infinit loops in case of hash table is full
                raise Exception ("Hash Table is full !")
            hash_code = (hash_code + 1) % self.Max
            probe += 1
        self.array[hash_code] = key, value
    

    # answer for the question 
    def __getitem__(self,key):
        hash_code = self.get_hash(key)
        probe = 0
        while self.array[hash_code] is not None and probe < self.Max:
            if self.array[hash_code][0] == key:
                return self.array[hash_code][1]
            hash_code = (hash_code + 1) % self.Max
            probe += 1

        return 'not found'


hashmap = HashTable()
hashmap['name'] = 'rahul'
hashmap['age'] = 20
print(hashmap['name'])
print(hashmap.array)

