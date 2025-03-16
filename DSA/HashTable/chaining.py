# hash table with chaining implementation 

class HashTable:

    def __init__(self, size):
        self.size = size
        self.array = [[]] * size
    
    def hash_function(self, key):
        return (sum(ord(i) for i in key) % self.size)

    def __setitem__(self, key, value):
        hash_code = self.hash_function(key)
        for index, element in enumerate(self.array[hash_code]):
            if element[0] == key :
                self.array[hash_code][index] = (key, value)
                return 
        self.array[hash_code].append((key, value))
    

    def __getitem__(self, key):
        hash_code = self.hash_function(key)
        for index, elment in enumerate(self.array[hash_code]):
            if elment[0] == key:
                return self.array[hash_code][index]
        return "not found"


r = HashTable(10)
r["key"] = "value"
r['abc'] = 'rahul'
r['bcd'] = 'another value'
print(r['key'])
print(r['abc'])
print(r['bcd'])


