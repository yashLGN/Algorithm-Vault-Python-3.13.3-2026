'''

HashTable Problem Statement

Description

Implement a HashTable class in Python that stores key-value pairs using a hash of the key. The hash table should handle collisions using nested dictionaries.

⸻

Requirements
	1.	The class should have a collection attribute initialized as an empty dictionary.
	2.	hash(key)
	•	Takes a string key.
	•	Returns a hashed value computed as the sum of ASCII values of each character in the string.
	3.	add(key, value)
	•	Adds a key-value pair to the hash table.
	•	Uses the hash of the key to store the pair in the collection.
	•	Handles collisions by storing multiple keys with the same hash in a nested dictionary.
	4.	remove(key)
	•	Deletes the key and its value from the hash table safely.
	5.	lookup(key)
	•	Returns the value associated with the key.
	•	Returns None if the key is not present.

'''

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in str(key))

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
