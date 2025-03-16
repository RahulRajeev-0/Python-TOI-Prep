# hash table implementation with double hashing

class HashTable:
    def __init__(self, max_size):
        self.Max = max_size
        self.array = [None] * self.Max

    def primary_hash(self, key):
       
        return sum(ord(char) for char in key) % self.Max

    def secondary_hash(self, key):
       
        return 1 + (sum(ord(char) for char in key) % (self.Max - 1))

    def __setitem__(self, key, value):
        hash_code = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        probe = 0
        
        
        while self.array[hash_code] is not None:
            if self.array[hash_code][0] == key:
               
                self.array[hash_code] = (key, value)
                return
            probe += 1
            if probe >= self.Max:
                raise Exception("HashTable is full!")
            
            hash_code = (hash_code + step_size) % self.Max
        self.array[hash_code] = (key, value)

    def __getitem__(self, key):
        hash_code = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        probe = 0

        
        while self.array[hash_code] is not None:
            if self.array[hash_code][0] == key:
                return self.array[hash_code][1]  
            probe += 1
            if probe >= self.Max:
                break  
            hash_code = (hash_code + step_size) % self.Max
        return "not found"  

    def __delitem__(self, key):
        hash_code = self.primary_hash(key)
        step_size = self.secondary_hash(key)
        probe = 0
        while self.array[hash_code] is not None:
            if self.array[hash_code][0] == key:
                self.array[hash_code] = None  
                return
            probe += 1
            if probe >= self.Max:
                break
            hash_code = (hash_code + step_size) % self.Max
        print("Key not found!") 

    

ht = HashTable(7)  
ht["apple"] = 10
ht["banana"] = 20
ht["grape"] = 30
print(ht["apple"])    
print(ht["banana"])   
print(ht["orange"])   
del ht["banana"]     
print(ht)            
