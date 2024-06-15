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
        h = 0
        for i in key:
            h += ord(i)
        return h % self.Max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        while self.array[h] is not None:
            h = (h + 1) % self.Max
        self.array[h] = key, value
    

    # answer for the question 
    def __getitem__(self,key):
        h = self.get_hash(key)
        while self.array[h] is not None:
            if self.array[h][0] == key:
                return self.array[h][1]
            h = (h + 1) % self.Max
        return 'not found'


hashmap = HashTable()
hashmap['name'] = 'rahul'
hashmap['age'] = 20
print(hashmap['name'])
print(hashmap.array)

