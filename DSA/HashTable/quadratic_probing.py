# quadratic probing implementation in hash table

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    
    def hash_function(self, key):
        return (sum(ord(i) for i in key)) % self.size
    
    def __setitem__(self, key, value):
        hash_code = self.hash_function(key)
        probe = 0
        while self.array[(hash_code + probe ** 2) % self.size] != None:
            probe += 1
            if probe >= self.size:
                raise Exception ("Hash Table is full")
            hash_code = ((hash_code + 1) ** 2) % self.size
        self.array[hash_code] = key, value
    
    def __getitem__(self, key):
        hash_code = self.hash_function(key)
        probe = 0 
        while self.array[(hash_code + probe ** 2) % self.size] != None:
            if self.array[(hash_code + probe ** 2) % self.size][0] == key:
                return self.array[(hash_code + probe ** 2) % self.size]
            probe += 1
            if probe >= self.size:
                break
        return "not found"
    
    def __repr__(self):
        return str(self.array)


h = HashTable(10)
h['name'] = 'rahul'
h['age'] = 20
print(h['age'])
print(h['name'])
print(h['email'])



