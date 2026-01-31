class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self,string1):
        string_list = list(string1)
        ascii_sum = 0
        for string in string_list:
            ascii_sum += ord(string)
        return ascii_sum

    def add(self, key, value):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}
        
    def remove(self, key):
        hashed_key = self.hash(key)
        
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]
    
    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None
    
# Create a HashTable instance
ht = HashTable()

# giving values
ht.add("apple", 10)
ht.add("banana", 20)
ht.add("papel", 30)  # same hash as "apple" so collision test

# Check internal structure
print(ht.collection)
# Expected: collision stored in nested dictionary

# Looking-up values
print("\nLookup keys:")
print("apple:", ht.lookup("apple"))   # 10
print("banana:", ht.lookup("banana")) # 20
print("papel:", ht.lookup("papel"))   # 30
print("orange:", ht.lookup("orange")) # None (key doesn't exist)

# Removing a key
ht.remove("apple")
print("\nAfter removing 'apple':")
print(ht.collection)
print("apple:", ht.lookup("apple"))   # None
print("papel:", ht.lookup("papel"))   # 30 still exists

# Removing a key causing nested dict to be empty
ht.remove("papel")
print("\nAfter removing 'papel':")
print(ht.collection)  # the hash for apple/papel should be gone

# Removing a key that doesnt exist
ht.remove("orange")   # Should not raise an error
print("\nAfter trying to remove non-existent key 'orange':")
print(ht.collection)
